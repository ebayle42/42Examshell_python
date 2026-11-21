int	digit_value(char c, int base)
{
	int	v;

	if (c >= '0' && c <= '9')
		v = c - '0';
	else if (c >= 'a' && c <= 'f')
		v = c - 'a' + 10;
	else if (c >= 'A' && c <= 'F')
		v = c - 'A' + 10;
	else
		return (-1);
	if (v >= base)
		return (-1);
	return (v);
}

int	ft_atoi_base(const char *str, int str_base)
{
	int	result;
	int	sign;
	int	v;

	result = 0;
	sign = 1;
	if (*str == '-')
	{
		sign = -1;
		str++;
	}
	while ((v = digit_value(*str, str_base)) >= 0)
	{
		result = result * str_base + v;
		str++;
	}
	return (result * sign);
}
