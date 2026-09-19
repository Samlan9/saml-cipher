# cipher
different cipher

---

這是一個用全部都用python寫的repo，有各種加密方式的程式，支援互動式加密，對使用者極度友善。

## 支援的加密方法：
- DES(不安全)
- AES-GCM-SIV
- RSA
- X448(with CHACHA20POLY1305)

DES:使用64bits的密鑰和CTR模式。  
AES:支援128､192､256bit的密鑰，更提供SIV模式來幫助減緩Nonce重複使用的風險。  
RSA:使用4096bit密鑰，結合了PKCS#1 OAEP。  
X448:使用了極為強大的X448加密演算法和非常節省資源的 CHACHA20POLY1305。  

* RSA､X448､DES提供測試用金鑰，請勿用於加密任何機密資訊。

---

## 開放原始碼授權條款：  
The pycryptodome module is copyrighted by Legrandin distributed under the following
BSD license.  

BSD license:

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
