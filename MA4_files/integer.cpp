#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();
	private:
		int val;
		int fibhelp(int);
	};

Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}

void Integer::set(int n){
	val = n;
	}



int Integer::fib(){
	return fibhelp(val);
	}

int Integer::fibhelp(int n){
	if((n==1)||(n==0)) {
   		return(n);
	}else {
		return(fibhelp(n-1)+fibhelp(n-2));
	}
	}



extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Integer_fib(Integer* integer) {return integer->fib();}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
