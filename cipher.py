from PIL import Image
import stepic

# from cryptography.fernet import Fernet
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend

class cipher_text(object):
	"""docstring for cipher_text"""
	def __init__(self,filename):
		self.filename = filename

	def encrypt(self,string, shift):
		cipher = ''
		for char in string:
			if char == ' ':
				cipher = cipher + char
			elif  char.isupper():
				cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
			else:
				cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
		return cipher

	def decrypt(self,string,shift):
	    cipher = ''
	    for char in string: 
	        if char == ' ':
	            cipher = cipher + char
	        elif  char.isupper():
	            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
	        else:
	            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
	    return cipher



	def encryption(self,filetype,info,key):

		location = 'static/'+self.filename
		image = Image.open(location)
		key = int(key)
		cipher_text = self.encrypt(info, key)

		cipher_text = bytes(cipher_text, 'utf-8')

		image = stepic.encode(image,cipher_text)
		image.save(location.split('.')[0]+'1.png','png')
		return True



	def decryption(self,key):

		location = 'static/userImage1.png'
		key = int(key)
		image = Image.open(location)
		info = stepic.decode(image)

		original_text = self.decrypt(info,key)
		return original_text
	

	#

	# def encrypt(key, message):
	#     f = Fernet(key)
	#     return f.encrypt(message.encode()).decode()

	# def decrypt(key, message):
	#     f = Fernet(key)
	#     return f.decrypt(message.encode()).decode()

	# def encode(image_path, key, message):
	#     """Encoding an encrypted message into an image."""
	#     encrypted_message = encrypt(key, message)
	#     img = Image.open(image_path)
	#     # Checking if the message can be encoded in the image
	#     max_bytes = img.size[0] * img.size[1] * 3 // 8
	#     if len(encrypted_message) > max_bytes:
	#         raise ValueError("Message too large for image.")
	#     # Converting message to binary
	#     encrypted_message += '\0'  # Adding null character to mark the end of the message
	#     bits = np.array([int(bit) for c in encrypted_message for bit in format(ord(c), "08b")])
	#     # Reshaping bits into 3 columns of pixels
	#     bits = bits.reshape(-1, 3)
	#     # Encoding bits into image pixels
	#     pixels = np.array(img)
	#     pixels = pixels.reshape(-1, 3)
	#     pixels[:, :] &= 0b11111110  # Clearing the least significant bit of each color component
	#     pixels[:, :] |= bits[:, :]  # Setting the least significant bit of each color component
	#     img_encoded = Image.fromarray(pixels.reshape(img.size))
	#     img_encoded.save(image_path.split('.')[0] + '_encoded.png')

	# def decode(image_path, key):
	#     """Decoding an encrypted message from an image."""
	#     img = Image.open(image_path)
	#     pixels = np.array(img)
	#     # Extracting the least significant bit from each color component of each pixel
	#     binary = np.unpackbits(pixels[:, :, :3] & 0b00000001)
	#     binary = binary.reshape(-1, 8)
	#     # Converting binary string to message
	#     encrypted_message = ''.join([chr(int(byte, 2)) for byte in binary.tolist()])
	#     encrypted_message = encrypted_message.split('\0')[0]
	#     message = decrypt(key, encrypted_message)
	#     return message


# encryption('vikash23.jpeg','image','My name is Vikash',2)

# decryption('vikash23.jpeg',2)
