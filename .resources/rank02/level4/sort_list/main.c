#include <stdio.h>
#include <stdlib.h>
#include "list.h"

t_list	*sort_list(t_list *lst, int (*cmp)(int, int));

static int	ascending(int a, int b) { return (a <= b); }
static int	descending(int a, int b) { return (a >= b); }

static t_list	*build(int argc, char **argv)
{
	t_list	*head = NULL;

	for (int i = argc - 1; i >= 1; i--)
	{
		t_list *node = malloc(sizeof(t_list));
		node->data = atoi(argv[i]);
		node->next = head;
		head = node;
	}
	return (head);
}

static void	print(const char *label, t_list *lst)
{
	printf("%s:", label);
	for (; lst; lst = lst->next)
		printf(" %d", lst->data);
	printf("\n");
}

int	main(int argc, char **argv)
{
	print("ascending", sort_list(build(argc, argv), ascending));
	print("descending", sort_list(build(argc, argv), descending));
	return (0);
}
