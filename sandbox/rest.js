var i = {
    "model": {
        "body": "Watson gives to Sherlock an array: $A_1, A_2, \\cdots, A_N$. He also gives to Sherlock two other arrays: $B_1, B_2, \\cdots, B_M$ and $C_1, C_2, \\cdots, C_M$.   \nThen Watson asks Sherlock to perform the following program:\n\n    for i = 1 to M do\n        for j = 1 to N do\n            if j % B[i] == 0 then\n                A[j] = A[j] * C[i]\n            endif\n        end do\n    end do\n\nCan you help Sherlock and tell him the resulting array $A$? You should print all the array elements modulo $(10^9 + 7)$.\n          \n**Input Format**     \nThe first line contains two integer numbers $N$ and $M$. The next line contains $N$ integers, the elements of array $A$. The next two lines contains $M$ integers each, the elements of array $B$ and $C$.\n\n**Output Format**     \nPrint $N$ integers, the elements of array $A$ after performing the program modulo $(10^9 + 7)$.\n\n**Constraints**  \n$1 \\le N, M \\le 10^5$   \n$1 \\le B[i] \\le N$   \n$1 \\le A[i], C[i] \\le 10^5$\n\n**Sample Input**\n\n\t4 3\n\t1 2 3 4\n\t1 2 3\n\t13 29 71\n    \n**Sample Output**\n\n\t13 754 2769 1508\t\n    \n",
        "body_html": "<div class='msB'><p><strong>Problem Statement</strong></p></div><div class='msB'><p>Watson gives to Sherlock an array: $A_1, A_2, \\cdots, A_N$. He also gives to Sherlock two other arrays: $B_1, B_2, \\cdots, B_M$ and $C_1, C_2, \\cdots, C_M$. <br>\nThen Watson asks Sherlock to perform the following program:</p>\n\n<pre><code>for i = 1 to M do\n    for j = 1 to N do\n        if j % B[i] == 0 then\n            A[j] = A[j] * C[i]\n        endif\n    end do\nend do\n</code></pre>\n\n<p>This code needs to be optimised. Can you help Sherlock and tell him the resulting array $A$? You should print all the array elements modulo $(10^9 + 7)$.</p>\n\n<p><strong>Input Format</strong> <br>\nThe first line contains two integer numbers $N$ and $M$. The next line contains $N$ integers, the elements of array $A$. The next two lines contains $M$ integers each, the elements of array $B$ and $C$.</p>\n\n<p><strong>Output Format</strong> <br>\nPrint $N$ integers, the elements of array $A$ after performing the program modulo $(10^9 + 7)$.</p>\n\n<p><strong>Constraints</strong> <br>\n$1 \\le N, M \\le 10^5$ <br>\n$1 \\le B[i] \\le N$ <br>\n$1 \\le A[i], C[i] \\le 10^5$</p>\n\n<p><strong>Sample Input</strong></p>\n\n<pre><code>4 3\n1 2 3 4\n1 2 3\n13 29 71\n</code></pre>\n\n<p><strong>Sample Output</strong></p>\n\n<pre><code>13 754 2769 1508    \n</code></pre></div>"
    }
}