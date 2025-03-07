from django.shortcuts import render
from django.views.generic import ListView, DetailView

from base.models import Item, Category, Tag


class IndexListView(ListView):
    """ トップページ用
    ItemテーブルからアイテムListを取得する
    指定が無ければ全データを取得し、「object_list」に格納する。
    """
    model = Item
    template_name = 'pages/index.html'
    queryset = Item.objects.filter(is_published=True)  # 追記

""" IndexListViewクラスを関数で記述する場合
def index(request):
    object_list = Item.objects.all()
    context = {
        'object_list': object_list,
    }
    return render(request, 'pages/index.html', context)
"""


class ItemDetailView(DetailView):
    """ 商品詳細ページ用
    個別のIDを元に個別のItemを取得しHTMLに渡す
    """
    model = Item
    template_name = 'pages/item.html'


class CategoryListView(ListView):
    """
    """
    model = Item # モデルはItem。カテゴリ単体を表示したいわけではなく、カテゴリを所持するアイテムを表示する為
    template_name = 'pages/list.html'
    paginate_by = 2 # ページに表示できるレコード数

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['pk'])
        return Item.objects.filter(is_published=True, category=self.category)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Category #{self.category.name}'
        return context


class TagListView(ListView):
    """
    """
    model = Item # モデルはItem。タグ単体を表示したいわけではなく、タグを所持するアイテムを表示する為
    template_name = 'pages/list.html'
    paginate_by = 2 # ページに表示できるレコード数

    def get_queryset(self):
        self.tag = Tag.objects.get(slug=self.kwargs['pk'])
        return Item.objects.filter(is_published=True, tags=self.tag)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Tag #{self.tag.name}'
        return context
