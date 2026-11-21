#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "flood_fill.h"

void	flood_fill(char **tab, t_point size, t_point begin);

/* argv: width height begin_x begin_y row1 row2 ... */
int	main(int argc, char **argv)
{
	if (argc < 5)
		return (0);
	t_point	size = {atoi(argv[1]), atoi(argv[2])};
	t_point	begin = {atoi(argv[3]), atoi(argv[4])};
	char	**area = malloc(sizeof(char *) * size.y);

	for (int i = 0; i < size.y; i++)
		area[i] = strdup(argv[5 + i]);
	flood_fill(area, size, begin);
	for (int i = 0; i < size.y; i++)
		printf("%s\n", area[i]);
	return (0);
}
