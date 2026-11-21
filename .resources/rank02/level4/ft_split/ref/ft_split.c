#include <stdlib.h>

int	is_sep(char c)
{
	return (c == ' ' || c == '\t' || c == '\n');
}

char	**ft_split(char *str)
{
	char	**tab;
	int		count;
	int		i;
	int		k;
	int		len;

	count = 0;
	i = 0;
	while (str[i])
	{
		while (str[i] && is_sep(str[i]))
			i++;
		if (str[i])
			count++;
		while (str[i] && !is_sep(str[i]))
			i++;
	}
	tab = malloc(sizeof(char *) * (count + 1));
	if (!tab)
		return (NULL);
	i = 0;
	k = 0;
	while (k < count)
	{
		while (is_sep(str[i]))
			i++;
		len = 0;
		while (str[i + len] && !is_sep(str[i + len]))
			len++;
		tab[k] = malloc(len + 1);
		len = 0;
		while (str[i] && !is_sep(str[i]))
			tab[k][len++] = str[i++];
		tab[k++][len] = '\0';
	}
	tab[k] = NULL;
	return (tab);
}
