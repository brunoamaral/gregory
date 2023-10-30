from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
from simple_history.models import HistoricalRecords
from django_countries.fields import CountryField

class Authors(models.Model):
	author_id = models.AutoField(primary_key=True)
	family_name = models.CharField(blank=False,null=False, max_length=150)
	given_name = models.CharField(blank=False,null=False, max_length=150)
	ORCID = models.CharField(blank=True, null=True, max_length=150, unique=True)
	country = CountryField(blank=True, null=True)  # New field
	orcid_check = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		full_name = (self.given_name,self.family_name)
		object_name = ' '.join(full_name)
		return str(object_name)
	class Meta:
		verbose_name_plural = 'authors'
		db_table = 'authors'
	@property
	def full_name(self):
		return self.given_name+" "+self.family_name

	
class Categories(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_description = models.TextField(blank=True, null=True)
	category_name = models.CharField(blank=True, null=True,max_length=200)
	category_slug = models.SlugField(blank=True, null=True, unique=True) # new field with unique=True
	category_terms = ArrayField(models.CharField(blank=False, null=False, max_length=100),default=list,verbose_name='Terms to include in category (comma separated)', help_text="Add terms separated by commas.")
	
	def save(self, *args, **kwargs):
		if not self.category_slug:
			self.category_slug = slugify(self.category_name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.category_name

	def article_count(self):
		return self.articles_set.count()
	
	class Meta:
		managed = True
		verbose_name_plural = 'categories'
		db_table = 'categories'


class Entities(models.Model):
	entity = models.TextField()
	label = models.TextField()

	class Meta:
		managed = True
		verbose_name_plural = 'entities'
		db_table = 'entities'

class Subject(models.Model):
	subject_name = models.CharField(blank=False,null=False, max_length=50)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return str(self.subject_name)


class Sources(models.Model):
	TABLES = [('science paper', 'Science Paper'),('trials','Trials'),('news article','News Article')]
	METHODS = [('rss', 'RSS'), ('scrape', 'Scrape'), ('manual', 'Manual submission')]
	source_id = models.AutoField(primary_key=True)
	source_for = models.CharField(choices=TABLES, max_length=50, default='science paper')
	name = models.TextField(blank=True, null=True)
	link = models.TextField(blank=True, null=True)
	language = models.TextField()
	subject = models.ForeignKey(Subject,on_delete=models.PROTECT,null=True,blank=True,unique=False)
	method = models.CharField(choices=METHODS, max_length=10, default='rss')
	ignore_ssl = models.BooleanField(default=False)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name or ""

	class Meta:
		managed = True
		verbose_name_plural = 'sources'
		db_table = 'sources'

class Articles(models.Model):
	KINDS = [('science paper', 'Science Paper'),('news article','News Article')]
	ACCESS_OPTIONS = [('unknown','Unknown'),('open','Open'),('restricted','Restricted')]
	article_id = models.AutoField(primary_key=True)
	title = models.TextField(blank=False, null=False, unique=True)
	link = models.URLField(blank=False, null=False, max_length=2000)
	doi = models.CharField(max_length=280, blank=True, null=True)
	summary = models.TextField(blank=True, null=True)
	source = models.ForeignKey(Sources, models.DO_NOTHING, db_column='source', blank=True, null=True,unique=False)
	published_date = models.DateTimeField(blank=True, null=True)
	discovery_date = models.DateTimeField(auto_now_add=True)
	authors = models.ManyToManyField(Authors, blank=True)
	categories = models.ManyToManyField(Categories)
	entities = models.ManyToManyField('Entities')
	relevant = models.BooleanField(blank=True, null=True)
	ml_prediction_gnb = models.BooleanField(blank=True, null=True)
	ml_prediction_lr = models.BooleanField(blank=True, null=True)
	noun_phrases = models.JSONField(blank=True, null=True)
	sent_to_admin = models.BooleanField(blank=True, null=True)
	sent_to_subscribers = models.BooleanField(blank=True, null=True)
	kind = models.CharField(choices=KINDS, max_length=50,default='science paper')
	access = models.CharField(choices=ACCESS_OPTIONS, max_length=50, default=None, null=True)
	publisher = models.CharField(max_length=150, blank=True, null=True, default=None)
	container_title = models.CharField(max_length=150, blank=True, null=True, default=None)
	crossref_check = models.DateTimeField(blank=True, null=True)
	takeaways = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return str(self.article_id)

	class Meta:
		managed = True
		unique_together = (('title', 'link'),)
		verbose_name_plural = 'articles'
		db_table = 'articles'

class Trials(models.Model):
	trial_id = models.AutoField(primary_key=True)
	discovery_date = models.DateTimeField(blank=True, null=True)
	title = models.TextField(blank=False,null=False, unique=True)
	summary = models.TextField(blank=True, null=True)
	link = models.URLField(blank=False, null=False, max_length=2000)
	published_date = models.DateTimeField(blank=True, null=True)
	source = models.ForeignKey('Sources', models.DO_NOTHING, db_column='source', blank=True, null=True, unique=False)
	relevant = models.BooleanField(blank=True, null=True)
	sent = models.BooleanField(blank=True, null=True)
	sent_to_subscribers = models.BooleanField(blank=True, null=True)
	sent_to_admin = models.BooleanField(blank=True,null=True, default=False)
	sent_real_time_notification = models.BooleanField(blank=True,null=True,default=False)
	categories = models.ManyToManyField(Categories,blank=True)
	identifiers = models.JSONField(blank=True,null=True)
	history = HistoricalRecords()
	def __str__(self):
		return str(self.trial_id) 

	class Meta:
		managed = True
		verbose_name_plural = 'trials'
		db_table = 'trials'

