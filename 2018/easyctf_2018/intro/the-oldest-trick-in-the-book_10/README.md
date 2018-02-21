# EasyCTF_2018: The Oldest Trick In the book

**Category:** Intro
**Points:** 10
**Description:**

>This is literally one of oldest tricks in the book. To be precise, from the year AD 56.
Crack me. wskqulx{o3du0e3_70_345qu7x_97wxww}

## Write-up
This one is also dead simple, simply use a site like [theblob](http://theblob.org/rot.cgi) and get all the possible ROT permutations. We see that at ROT-8, we get our flag!

    ROT-0: wskqulx{o3du0e3_70_345qu7x_97wxww}
    ROT-1: xtlrvmy{p3ev0f3_70_345rv7y_97xyxx}
    ROT-2: yumswnz{q3fw0g3_70_345sw7z_97yzyy}
    ROT-3: zvntxoa{r3gx0h3_70_345tx7a_97zazz}
    ROT-4: awouypb{s3hy0i3_70_345uy7b_97abaa}
    ROT-5: bxpvzqc{t3iz0j3_70_345vz7c_97bcbb}
    ROT-6: cyqward{u3ja0k3_70_345wa7d_97cdcc}
    ROT-7: dzrxbse{v3kb0l3_70_345xb7e_97dedd}
    ROT-8: easyctf{w3lc0m3_70_345yc7f_97efee}
    ROT-9: fbtzdug{x3md0n3_70_345zd7g_97fgff}
    ROT-10: gcuaevh{y3ne0o3_70_345ae7h_97ghgg}
    ROT-11: hdvbfwi{z3of0p3_70_345bf7i_97hihh}
    ROT-12: iewcgxj{a3pg0q3_70_345cg7j_97ijii}
    ROT-13: jfxdhyk{b3qh0r3_70_345dh7k_97jkjj}
    ROT-14: kgyeizl{c3ri0s3_70_345ei7l_97klkk}
    ROT-15: lhzfjam{d3sj0t3_70_345fj7m_97lmll}
    ROT-16: miagkbn{e3tk0u3_70_345gk7n_97mnmm}
    ROT-17: njbhlco{f3ul0v3_70_345hl7o_97nonn}
    ROT-18: okcimdp{g3vm0w3_70_345im7p_97opoo}
    ROT-19: pldjneq{h3wn0x3_70_345jn7q_97pqpp}
    ROT-20: qmekofr{i3xo0y3_70_345ko7r_97qrqq}
    ROT-21: rnflpgs{j3yp0z3_70_345lp7s_97rsrr}
    ROT-22: sogmqht{k3zq0a3_70_345mq7t_97stss}
    ROT-23: tphnriu{l3ar0b3_70_345nr7u_97tutt}
    ROT-24: uqiosjv{m3bs0c3_70_345os7v_97uvuu}
    ROT-25: vrjptkw{n3ct0d3_70_345pt7w_97vwvv}

Therefore, the flag is `ROT-8: easyctf{w3lc0m3_70_345yc7f_97efee}`.
