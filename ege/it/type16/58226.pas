var n: longint;
function F(n: longint): longint;
	begin
	if n = 1
		then F := 1
	else if n = 2
		then F := 2
	else if ((n mod 2) = 0)
		then F := round((3 * n + F(n - 3)) / 3)
	else if (((n mod 2) = 1) and (n > 2))
		then F := round((7 * n + F(n - 1) - F(n - 2)) / 5)
end;
begin
	n := F(35);
	writeln(n);
end.

