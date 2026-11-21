#include "list.h"

t_list	*sort_list(t_list *lst, int (*cmp)(int, int))
{
	t_list	*a;
	t_list	*b;
	int		tmp;

	a = lst;
	while (a)
	{
		b = a->next;
		while (b)
		{
			if (!cmp(a->data, b->data))
			{
				tmp = a->data;
				a->data = b->data;
				b->data = tmp;
			}
			b = b->next;
		}
		a = a->next;
	}
	return (lst);
}
