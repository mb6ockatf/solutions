function f(n: longint): longint;
begin
	if n >= 2025
		then f := n
	else if n < 2025
		then f := n + f(n + 2);
end;

begin
	writeln(f(2022) - f(2023));
end.
