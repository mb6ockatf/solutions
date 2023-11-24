Program TwoEightOneTwoOne;
var
	i, j, divisors, counter: longint;
begin
	counter := 1;
	for i := 2422000 to 2422080 do begin
		divisors := 0;
		for j := 2 to i div 2 do begin
			if i mod j <> 0 then continue;
			divisors := -1;
			break;
		end;
		if divisors = 0 then begin
			writeln(counter, ' ', i);
			counter := counter + 1;
		end;
	end;
end.
