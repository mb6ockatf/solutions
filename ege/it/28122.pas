Program TwoEightOneTwoTwo;
var
	j, k, divisors: longint;
	res: array[1..2] of longint;
begin
	for j := 489421 to 489440 do begin
		divisors := 0;
		for k := 2 to (j div 2) do begin
			if (j mod k) <> 0 then continue;
			divisors := divisors + 1;
			if divisors > 2 then break;
			res[divisors] := k;
		end;
		if divisors = 2 then begin
			writeln(1, ' ', res[1], ' ', res[2], ' ', j);
		end;
	end;
end.
