#include <stdio.h>
#include <stdlib.h>
#include "ft_list.h"

int	ft_list_size(t_list *begin_list);

int	main(int argc, char **argv)
{
	t_list	*head = NULL;

	printf("%d\n", ft_list_size(NULL));
	for (int i = argc - 1; i >= 1; i--)
	{
		t_list *node = malloc(sizeof(t_list));
		node->data = argv[i];
		node->next = head;
		head = node;
		printf("%d\n", ft_list_size(head));
	}
	return (0);
}
