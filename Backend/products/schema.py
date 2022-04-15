import graphene
from graphene_django import DjangoObjectType
from .models import (Product,Category,SubCategory,ProductImage,Rating,Comment)

class ProductsType(DjangoObjectType):
    class Meta:
        model=Product

    def resolve_all_Products(root,info):
        return Product.objects.all()
    
    def resolve_product(root,info,id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return None

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
    def resolve_category(root,info,id,name=None):
        try:
            if(id):
                return Category.objects.get(pk=id)
            if(name):
                return Category.objects.get(name=name)
            else:
                return None
        except Category.DoesNotExist:
            return None

class SubCategoryType(DjangoObjectType):
    class Meta:
        model=SubCategory

class ProductImageType(DjangoObjectType):
    class Meta:
        model=ProductImage
        fields=('id','image')
    def resolve_image(self,info):
        if self.image:
            self.image=info.context.build_absolute_uri(self.image.url)
        return self.image

class RatingType(DjangoObjectType):
    class Meta:
        model=Rating
        fields=('id',"note")

class CommentType(DjangoObjectType):
    class Meta:
        model=Comment
        fields=('id','body')

class Query(graphene.ObjectType):
    all_Products=graphene.List(ProductsType)
    product=graphene.Field(ProductsType,id=graphene.Int())
    category=graphene.Field(CategoryType,id=graphene.Int(),name=graphene.String())



        

