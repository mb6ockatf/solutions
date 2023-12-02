var n: longint = 0;
var i: longint;
function f(n: longint): longint;
begin
	if n = 0 then f := 0
	else if (n > 0) and ((n mod 2) = 0)
		then f := f(round(n / 2))
	else if ((n mod 2) = 1) then f := 1 + f(n - 1);
end;
begin
	for i := 1 to 1000 do begin
		if f(i) = 3 then
			n := n + 1;
	end;
	writeln(n);
end.
