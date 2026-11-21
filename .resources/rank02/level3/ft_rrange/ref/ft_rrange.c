#include <stdlib.h>

int	*ft_rrange(int start, int end)
{
	int	*tab;
	int	len;
	int	i;
	int	step;

	len = (start > end ? start - end : end - start) + 1;
	tab = malloc(sizeof(int) * len);
	if (!tab)
		return (NULL);
	step = (end <= start) ? 1 : -1;
	i = 0;
	while (i < len)
	{
		tab[i] = end + i * step;
		i++;
	}
	return (tab);
}
