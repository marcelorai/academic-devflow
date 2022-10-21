from django.views.generic import UpdateView

from projects.models import Projeto


class ProjetoUpdateView(UpdateView):
    model = Projeto
    fields = '__all__'

    def get_success_url(self):
        return '/'


update_view = ProjetoUpdateView.as_view()
