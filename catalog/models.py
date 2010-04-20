from django.db import models

class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set(). \
                                                        filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
            help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
         help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
         help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'
    
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), { 'category_slug': self.slug })
    
    objects = models.Manager()
    active = ActiveCategoryManager()

class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set(). \
                                                        filter(is_active=True)

class FeaturedProductManager(models.Manager):
    def all(self):
        return super(FeaturedProductManager, self).all(). \
                                filter(is_active=True).filter(is_featured=True)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
         help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True,
                                    default=0.00)
    image = models.ImageField(upload_to='images/products/main')
    thumbnail = models.ImageField(upload_to='images/products/thumbnails')
    image_caption = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255,
                help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField(max_length=255,
                                help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    
    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.name
 
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product', (), { 'product_slug': self.slug })
 
    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
    
    objects = models.Manager()
    active = ActiveProductManager()
    featured = FeaturedProductManager()
    
    def cross_sells(self):
        from ecomstore.checkout.models import Order, OrderItem
        orders = Order.objects.filter(orderitem__product=self)
        order_items = OrderItem.objects.filter(order__in=orders). \
                                                        exclude(product=self)
        products = Product.active.filter(orderitem__in=order_items).distinct()
        return products

    def cross_sells_user(self):
        from ecomstore.checkout.models import Order, OrderItem
        from django.contrib.auth.models import User
        users = User.objects.filter(order__orderitem__product=self)
        items = OrderItem.objects.filter(order__user__in=users).exclude(
                                                                product=self)
        products = Product.active.filter(orderitem__in=items).distinct()
        return products

    def cross_sells_hybrid(self):
        from ecomstore.checkout.models import Order, OrderItem
        from django.contrib.auth.models import User
        from django.db.models import Q
        orders = Order.objects.filter(orderitem__product=self)
        users = User.objects.filter(order__orderitem__product=self)
        items = OrderItem.objects.filter( Q(order__in=orders) |
                      Q(order__user__in=users)
                      ).exclude(product=self)
        products = Product.active.filter(orderitem__in=items).distinct()
        return products
