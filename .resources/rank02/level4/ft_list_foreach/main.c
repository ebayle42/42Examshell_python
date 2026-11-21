#include <stdio.h>
#include <stdlib.h>
#include "ft_list.h"

void	ft_list_foreach(t_list *begin_list, void (*f)(void *));

static void	print_data(void *data)
{
	printf("[%s]", (char *)data);
}

static void	upper_first(void *data)
{
	char *s = data;
	if (s[0] >= 'a' && s[0] <= 'z')
		s[0] -= 32;
}

int	main(int argc, char **argv)
{
	t_list	*head = NULL;

	ft_list_foreach(NULL, print_data);
	for (int i = argc - 1; i >= 1; i--)
	{
		t_list *node = malloc(sizeof(t_list));
		node->data = argv[i];
		node->next = head;
		head = node;
	}
	ft_list_foreach(head, print_data);
	printf("\n");
	ft_list_foreach(head, upper_first);
	ft_list_foreach(head, print_data);
	printf("\n");
	return (0);
}
