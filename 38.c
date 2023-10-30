char * countAndSay(int n){
	
    if (n == 1) return "1";
	
	
	char *response = countAndSay(n-1); 
	char *newresponse = malloc(strlen(response) * (n > 20 ? 2 : 3)); 
	int ctr, curpos=0; 
	char curval, *iter=response;
	char *head = response; 

	
	while (*response){
		
		ctr = 0;
		curval = *response;
		while (*iter && *iter == curval){
			
			ctr++;
			iter++;
		}
		
		newresponse[curpos] = ctr + '0';
		newresponse[curpos+1] = curval;
		curpos += 2;
		response = iter;
	}
	
	newresponse[curpos] = '\0';
	curpos++;
	
	newresponse = realloc(newresponse, curpos);
	
	
	if (n > 2) free(head);
	return newresponse;
}
