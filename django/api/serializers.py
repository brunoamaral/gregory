from django.contrib.auth.models import User, Group
from django.db.models.fields import SlugField
from rest_framework import serializers
from gregory.models import Articles, Trials, Sources, Authors, Categories

class CategorySerializer(serializers.ModelSerializer):
	count_of_articles = serializers.SerializerMethodField()

	class Meta:
		model = Categories
		fields = ['category_id', 'category_description', 'category_name', 'category_slug', 'category_terms','count_of_articles']

	def get_count_of_articles(self, obj):
		return obj.article_count()

class ArticleAuthorSerializer(serializers.ModelSerializer):
	country = serializers.SerializerMethodField()

	class Meta:
		model = Authors
		fields = ['author_id', 'given_name', 'family_name', 'ORCID', 'country']

	def get_country(self, obj):
		if obj.country:
			return obj.country.code  # or obj.country.name depending on what you want to display
		return None

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	source = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	categories = CategorySerializer(many=True, read_only=True)
	authors = ArticleAuthorSerializer(many=True, read_only=True)  # Update this line to use the new serializer
	class Meta:
		model = Articles
		depth = 1
		fields = ['article_id','title','summary','link','published_date','source','publisher','container_title','authors','relevant','ml_prediction_gnb','ml_prediction_lr','ml_prediction_lsvc','discovery_date','noun_phrases','doi','access','takeaways','categories']
		read_only_fields = ('discovery_date','ml_prediction_gnb','ml_prediction_lr','ml_prediction_lsvc','noun_phrases','takeaways')

class TrialSerializer(serializers.HyperlinkedModelSerializer):
	source = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
	categories = CategorySerializer(many=True, read_only=True)

	class Meta:
		model = Trials
		fields = ['trial_id','title','summary','published_date','discovery_date','link','source','relevant','identifiers','categories', 'export_date', 'internal_number', 'last_refreshed_on', 
            'scientific_title', 'primary_sponsor', 'retrospective_flag', 'date_registration', 
            'source_register', 'recruitment_status', 'other_records', 'inclusion_agemin', 
            'inclusion_agemax', 'inclusion_gender', 'date_enrollement', 'target_size', 
            'study_type', 'study_design', 'phase', 'countries', 'contact_firstname', 
            'contact_lastname', 'contact_address', 'contact_email', 'contact_tel', 
            'contact_affiliation', 'inclusion_criteria', 'exclusion_criteria', 'condition', 
            'intervention', 'primary_outcome', 'secondary_outcome', 'secondary_id', 
            'source_support', 'ethics_review_status', 'ethics_review_approval_date', 
            'ethics_review_contact_name', 'ethics_review_contact_address', 'ethics_review_contact_phone', 
            'ethics_review_contact_email', 'results_date_completed', 'results_url_link']
		read_only_fields = ('discovery_date',)
		
class SourceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sources
		fields = ['name','description','source_id','source_for','link']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
	articles_count = serializers.SerializerMethodField()
	country = serializers.SerializerMethodField()
	class Meta:
		model = Authors
		fields = ['author_id','given_name','family_name','ORCID', 'country', 'articles_count']
	def get_articles_count(self, obj):
		return obj.articles_set.count()
	def get_country(self, obj):
		if obj.country:
			return obj.country.code  # or obj.country.name depending on what you want to display
		return None
class CountArticlesSerializer(serializers.ModelSerializer):
	articles_count = serializers.SerializerMethodField()

	class Meta:
		model = Articles
		fields = ( 'articles_count',)   

	def get_articles_count(self, obj):
		return Articles.objects.all().count()