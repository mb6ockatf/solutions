Program TwoSevenEightFiveEight;
var
	i, j, maximal_num, maximal_divisors, divisors: longint;
begin
	maximal_num := 0; maximal_divisors := 0;
	for i := 120115 to 120200 do begin
		divisors := 2; (* i and 1 include *)
		for j := 2 to (i div 2) do begin
			if (i mod j <> 0) then continue;
			divisors := divisors + 1;
		end;
		if (maximal_divisors = divisors) and (maximal_num < i) then
			maximal_num := i;
		if (maximal_divisors < divisors) then begin
			maximal_divisors := divisors;
			maximal_num := i;
		end;
	end;
	writeln(maximal_divisors, ' ', maximal_num);
end.
