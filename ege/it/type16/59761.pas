function f(n: longint): longint;
begin
	if n < 11 then f := 10
	else if n >= 11
		then f := n + f(n - 1);
end;
begin
	writeln(f(2124) - f(2122));
end.
