#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ft_list.h"

void	ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)());

int	main(int argc, char **argv)
{
	t_list	*head = NULL;
	t_list	*empty = NULL;

	if (argc < 2)
		return (0);
	ft_list_remove_if(&empty, argv[1], strcmp);
	printf("empty: %s\n", empty ? "not NULL" : "NULL");
	for (int i = argc - 1; i >= 2; i--)
	{
		t_list *node = malloc(sizeof(t_list));
		node->data = argv[i];
		node->next = head;
		head = node;
	}
	ft_list_remove_if(&head, argv[1], strcmp);
	printf("remove [%s]:", argv[1]);
	for (t_list *p = head; p; p = p->next)
		printf(" [%s]", (char *)p->data);
	printf("\n");
	return (0);
}
