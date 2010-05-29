from scipy import array

def read_dipole_excitation(filename):
        # the structure of the excitation file must be as follows:
        # 1 line per dipole, as many lines as there are dipoles
        # each line has 9 columns that must be arranged as follows:
        #
        # real(J_x) imag(J_x) real(J_y) imag(J_y) real(J_z) imag(J_z) r_x r_y r_z
        #
        # where J = [J_x J_y J_z] is the dipole and r = [r_x r_y r_z] its origin.
        r_tmp, J_tmp = [], []
        excitation_file = open(filename, 'r')
        for line in excitation_file:
            elems = line.split()
            if (len(elems)==9) and (elems!=[]):
                r_tmp.append(map(float, elems[6:]))
                J_tmp.append(map(float, elems[:6]))
        r_src = array(r_tmp, 'd')
        J_tmp2 = array(J_tmp, 'd')
        J_src = array(J_tmp2[:,0:6:2], 'd') + array(J_tmp2[:,1:6:2], 'd') * 1.j
        return J_src, r_src
