function f(n: longint): longint;
begin
	if n < 7
		then f:= 7
	else if n >= 7
		then f := 2 * n + f(n - 1);
end;
begin
	writeln(f(2024) - f(2022));
end.
