program TwoEightOneTwoThree;
var
	j, k, divisors: longint;
	res: array[1..6] of longint;
begin
	for j := 125256 to 125330 do begin
		divisors := 0;
		for k := 1 to j do begin
			if (j mod k = 0) and (k mod 2 = 0) then begin
				divisors := divisors + 1;
				if divisors > 6 then break;
				res[divisors] := k;
			end;
		end;
		if divisors = 6 then writeln(1, ' ', res[2], ' ', res[3], ' ',
			res[4], ' ', res[5], ' ', j);
	end;
end.
