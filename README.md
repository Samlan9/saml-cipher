# cipher

這是一個用全部都用python寫的repo，有各種加密方式的程式，支援互動式加密，對使用者極度友善。

## 支援的加密方法：
- [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard)(不安全)
- [AES-GCM-SIV](https://en.wikipedia.org/wiki/AES-GCM-SIV)     
- [RSA](https://en.wikipedia.org/wiki/RSA_cryptosystem)
- [X448](https://en.wikipedia.org/wiki/Curve448)(with [CHACHA20POLY1305](https://en.wikipedia.org/wiki/ChaCha20-Poly1305))

DES:使用64bits的密鑰和CTR模式。  
AES:支援128､192､256bit的密鑰，更提供SIV模式來幫助減緩Nonce重複使用的風險。  
RSA:使用4096bit密鑰，結合了[PKCS#1 OAEP](https://en.wikipedia.org/wiki/PKCS_1)。  
X448:使用了極為強大的X448加密演算法和非常節省資源的 CHACHA20POLY1305。  

RSA､X448､DES提供測試用金鑰，請勿用於加密任何機密資訊(密碼：`test`)。

---

## 如何使用？
只須找到對應資料夾裡的.py檔案並直接運行即可！

加密：
<img width="2851" height="672" alt="RSA加密範例圖片" src="https://github.com/user-attachments/assets/d989773f-dc66-43ee-92bb-0e720d784430" />

解密：
<img width="999" height="276" alt="RSA解密範例圖片" src="https://github.com/user-attachments/assets/14116e49-56c3-47cf-9c16-d7df882bfa60" />

---

## 開放原始碼授權條款：  
##### The pycryptodome module is copyrighted by Legrandin distributed under the following BSD license.  

All direct contributions to PyCryptodome are released under the following
license. The copyright of each piece belongs to the respective author.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


##### The questionary module is copyrighted by Tom Bocklisch and contributors distributed under the following MIT license.  

Copyright 2020 Tom Bocklisch and contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

我已盡全力處理所有著作權和許可事宜。如有任何疏漏，請立即告知—我非常樂意改正。感謝您的理解與支持！
I’ve tried my absolute best to handle all copyright and licensing matters properly. If I happened to miss something, please let me know right away—I’m more than happy to make it right. Thank you for your grace and support!
