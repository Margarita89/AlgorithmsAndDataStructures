# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

# checks if it's possible to insert 1 character into s2
def checkInsert(s1, s2):
    # index of current s1
    ind1 = 0
    ind2 = 0
    #number of inserts in s2
    insert = 0
    # run through s2
    while ind2 < len(s2) and ind1 < len(s1):
        if s1[ind1] == s2[ind2]:
            ind1 += 1
            ind2 += 1
        else:
            insert += 1
            ind1 += 1
            if insert > 1:
                return False
    # includes situation when insert =0, but the last character was not tested in s1 - so insert it in s2
    return True


# checks if it's possible to delete 1 character from s1
def checkDelete(s1, s2):
    ind1 = 0
    ind2 = 0
    # number of deletes in s1
    delete = 0
    while ind1 < len(s1) and ind2 < len(s2):
        if s1[ind1] == s2[ind2]:
            ind1 += 1
            ind2 += 1
        else:
            delete += 1
            ind1 += 1
            if delete > 1:
                return False
    # includes situation when no deletion in s1, but last character remains in s1 when we finish while, so delete it to get s2
    return True


# checks if it's possible to replace 1 character in s1
def checkReplace(s1, s2):
    ind1 = 0
    ind2 = 0
    replace = 0
    while ind1 < len(s1) and ind2 < len(s2):
        if s1[ind1] != s2[ind2]:
            replace += 1
        ind1 += 1
        ind2 += 1
        if replace > 1:
            return False
    return True


# checks if s1 and s2 are one away character from each other
def OneAway(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    # if s1 is longer than s2 - check if it's possible to insert 1 character into s2
    # similarly, it's possible but REDUNDANT to check if it's possible to delete 1 character from s1
    if len_s1 - len_s2 == 1:
        check_ins = checkInsert(s1, s2)
        print('check_ins  1 : ', check_ins)
        check_del = checkDelete(s1, s2)
        print('check_del  1 : ', check_del)
        return (check_ins and check_del)
    #(len_s1 = len_s2)
    else:
        check_rep = checkReplace(s1, s2)
        print('check_rep  3 : ', check_rep)
        return check_rep


if __name__ == "__main__":

    #s1, s2 = input().split()
    s1 = 'pale'
    s2 = 'bake'
    # check if difference in length is more than 1
    if abs(len(s1) - len(s2)) > 1:
        print(False)
    else:
        arr_s1 = [ch for ch in s1]
        arr_s2 = [ch for ch in s2]
        # chooses short and long string
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        print(OneAway(s1, s2))

        #s1, s2 = input().split()
    s1 = 'pale'
    s2 = 'bale'
    # check if difference in length is more than 1
    if abs(len(s1) - len(s2)) > 1:
        print(False)
    else:
        arr_s1 = [ch for ch in s1]
        arr_s2 = [ch for ch in s2]
        # chooses short and long string
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        print(OneAway(s1, s2))
