from django.db import models


class RootCatagory(models.Model):
    """Model definition for RootCatagory."""

    root_cat = models.CharField(max_length=50)

    class Meta:
        """Meta definition for RootCatagory."""

        verbose_name = 'RootCatagory'
        verbose_name_plural = 'RootCatagory'

    def __str__(self):
        """Unicode representation of RootCatagory."""
        return self.root_cat

class Catagory(models.Model):
    """Model definition for Catagories."""

    cat_name  = models.CharField(max_length=50, unique=True)
    par_cat   = models.ForeignKey(RootCatagory, on_delete=models.CASCADE, null=True)
    cat_title = models.CharField(choices=[('show', 'show'), ('hide', 'hide')], max_length=4, null=True)
    cat_icon  = models.ImageField(upload_to='cat_icons', default="cat_icons/AdminLTELogo.png", blank=True)
    cat_desc  = models.TextField(null=True)
    clr_url   = models.CharField(max_length=50, null=True)
    is_enable = models.BooleanField(max_length=50, default=True)

    class Meta:
        """Meta definition for Catagories."""

        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagory'

    def __str__(self):
        """Unicode representation of Catagories."""
        return self.cat_name


class SubCatagory(models.Model):
    """Model definition for SubCatagory."""
    cat_name  = models.CharField(max_length=50, unique=True)
    par_cat   = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True)
    cat_title = models.CharField(choices=[('show', 'show'), ('hide', 'hide')], max_length=4, null=True, blank=True)
    cat_icon  = models.ImageField(upload_to='cat_icons', default="cat_icons/AdminLTELogo.png", blank=True)
    cat_desc  = models.TextField(null=True, blank=True)
    clr_url   = models.CharField(max_length=50, null=True, blank=True)
    is_enable = models.BooleanField(max_length=50, default=True,blank=True)
    meta_key = models.CharField(max_length=50, null=True, blank=True) 
    meta_desc = models.CharField(max_length=50, null=True, blank=True) 

    class Meta:
        """Meta definition for SubCatagory."""

        verbose_name = 'SubCatagory'
        verbose_name_plural = 'SubCatagory'

    def __str__(self):
        """Unicode representation of SubCatagory."""
        return self.cat_name


class Products(models.Model):
    """basic information."""
    catagory               = models.ManyToManyField(SubCatagory)
    prod_name              = models.CharField(max_length=50, null=True)
    sku                    = models.CharField(max_length=50, null=True)
    weight                 = models.CharField(max_length=50, null=True)
    prod_size              = models.CharField(choices=[('S', 'S'),('M', 'M'),('L', 'L')], max_length=2, null=True) 
    
    arrival_date           = models.DateField(null=True)
    prod_img               = models.ImageField(upload_to='products', null=True)
    prod_desc              = models.TextField(null=True)

    price                  = models.IntegerField(null=True)
    sell_price             = models.IntegerField(null=True)
    shipping_price         = models.IntegerField(null=True)
    quantity_in_stock      = models.IntegerField(null=True)

    req_shipping           = models.BooleanField(null=True)
    is_free                = models.BooleanField(null=True)
    is_inventory_track     = models.BooleanField(null=True)
    allow_to_attach_file   = models.BooleanField(null=True)
    is_mandatory_to_attach = models.BooleanField(null=True)
    is_avail_to_sell       = models.BooleanField(null=True)

    class Meta:
        """Meta definition for Products."""

        verbose_name = 'Products'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Products."""
        return self.prod_name


class RelProducts(models.Model):
    """Model definition for RelProducts."""
    prod_id = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for RelProducts."""

        verbose_name = 'RelProducts'
        verbose_name_plural = 'RelProducts'

    def __str__(self):
        """Unicode representation of RelProducts."""
        return self.prod_name

class ProductsReview(models.Model):
    """Model definition for Products."""

    prod_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    rating = models.CharField(max_length=50)
    reviewer_name = models.CharField(max_length=50)
    text_of_review = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Products."""

        verbose_name = 'ProductsReview'
        verbose_name_plural = 'ProductsReview'

    def __str__(self):
        """Unicode representation of Products."""
        return self.prod_id.prod_name
