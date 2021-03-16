import traceback as tb


class Test:


    # Takes in a function f and a list of tuples which correspond to the
    # function input/s for each case.

    # Also takes in lists of messages to print the input (input_print) and the output (output_print) of each method
    # call for each case in cases_args. The output_print should only be passed if the function passed is
    # in-place. You must format each message in output_print so that it prints a particular object.
    # If the function f is not in-place, then you may leave output_print as None by default and pass in print_f_out
    # as true. You may also pass in output_print as a populated list and print_f_out as True, and this will print
    # the in-place modified object as well as the output of f.

    # By default the parameter print_trace is set to True. This parameter
    # indicates whether the error trace log will be printed if a method
    # encounters an error. If print_trace is False, the test will just print
    # the type of error to the terminal if there is an error.

    def __init__(self, f, cases_args, input_print, output_print=None, print_f_out=False, print_trace=True):
        self.f = f
        self.cases_args = cases_args
        self.input_print = input_print
        self.output_print = output_print
        self.print_f_out = print_f_out
        self.print_trace = print_trace


    # Calling .run() on a Test object will run the function f on all test cases
    # and print the given input, output, and returns of the function if applicable.
    # It will also print the error log trace if print_trace = True, else it will just
    # print the error message. It will only print error message/trace if the function
    # throws an error for any one of the cases. If there is an error, the rest of the
    # cases will still be tested.
    def run(self):
        for i in range(len(self.cases_args)):
            print("\n")
            if self.input_print[i][1] != None:
                print("{} {}".format(self.input_print[i][0], self.input_print[i][1].to_string()))
            else:
                print("{} {}".format(self.input_print[i][0], self.input_print[i][1]))
            if self.print_f_out:
                out = "No output"
                try:
                    out = self.f(*self.cases_args[i])
                except Exception as ex:
                    if self.print_trace:
                        print(tb.format_exc())
                    else:
                        print(ex)
                if self.output_print != None:
                    if self.output_print[i][1] != None:
                        print("{} {}".format(self.output_print[i][0], self.output_print[i][1].to_string()))
                    else:
                        print("{} {}".format(self.output_print[i][0], self.output_print[i][1]))
                print("Function returned: {}".format(out))
            else:
                try:
                    self.f(*self.cases_args[i])
                except Exception as ex:
                    if self.print_trace:
                        print(tb.format_exc())
                    else:
                        print(ex)
                if self.output_print != None:
                    if self.output_print[i][1] != None:
                        print("{} {}".format(self.output_print[i][0], self.output_print[i][1].to_string()))
                    else:
                        print("{} {}".format(self.output_print[i][0], self.output_print[i][1]))
        print("\n")
