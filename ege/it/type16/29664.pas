var n: longint;
function F(n: longint): longint;
	begin
	if n = 1
		then F := 1
	else if ((n mod 2) = 0)
		then F := n * F(n - 1)
	else if (((n mod 2) = 1) and (n > 1))
	then F := n + F(n - 2);
end;
begin
	n := F(60);
	writeln(n);
end.
