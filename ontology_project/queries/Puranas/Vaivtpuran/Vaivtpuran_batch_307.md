# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 13.12282)
- **Original**: दुर्गतिनाशिनी दुर्गाका ध्यान करते हैं। गया है। पतिकी कामना रखनेवाली स््रियोंको दुर्गाका ध्यान उनकी इच्छाके अनुसार फल देनेवाला है। इससे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.12283)
- **Original**: . भगवती दुर्गा शिवा (कल्याणस्वरूपा), प्रियतम पति-निर्मित्तक फलकी प्राप्ति होती है। शिवप्रिया, शैवी (शिवसे प्रगाढ़ सम्बन्ध रखनेवाली ) कुमारी कन्याकों चाहिये कि वह पहले दिन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.12284)
- **Original**: तथा शिवके वक्ष:स्थलपर विराजमान होनेबाली उपवास करके अपने वस्त्रकों धो डाले और हैं। उनके प्रसन्न मुखपर मन्द मुस्कानकी प्रभा संयमपूर्वक रहे। फिर मार्गशीर्ष मासकी संक्रान्तिके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.12285)
- **Original**: फैली रहती है। उनकी बड़ी प्रतिष्ठा है। उनके दिन प्रातःकाल श्रद्धापूर्वक नदीके तटपर जाकर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.12286)
- **Original**: नेत्र मनोहर हैं। वे नित्य नूतन यौवनसे सम्पन्न स्नान करके वह दो धुले हुए वस्त्र (साड़ी और
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.12287)
- **Original**: हैं और रत्रमय आभूषण धारण करती हैं। उनकी चोली) धारण करे। तत्पश्चात्‌ कलशमें गणेश,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.12288)
- **Original**: भुजाएँ रत्नमय केयूर तथा कह्कूणोंसे और दोनों सूर्य, अग्नि, विष्णु, शिव और दुर्गा (पार्वती )--इन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.12289)
- **Original**: चरण रल्ननिर्मित नूपुरोंसे विभूषित हैं। रत्नोंके बने छ: देवताओंका आबाहन करके नाना द्रव्योंद्वारा हुए दो कुण्डल उनके दोनों कपोलॉंकी शोभा उनका पूजन करें। इन सबका पश्ञोपचार पूजन बढ़ाते हैं। उनकी वेणीमें मालतीकी माला लगी करके वह ब्रत आरम्भ करे। कलशके सामने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.12290)
- **Original**: हुई है, जिसपर भ्रमर मँड्राते रहते हैं। भालदेशमें नीचे भूमिपर एक सुविस्तृत बेदी बनावे। वह
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.12291)
- **Original**: कस्तूरीकी बेंदीके साथ सिन्दूरका सुन्दर तिलक बेदी चौकोर होनी चाहिये। चन्दन, अगुरु, कस्तूरी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.12292)
- **Original**: शोभा पाता है। उनके दिव्य वस्त्र अग्निकी और कुंकुमसे उस वेदीका संस्कार करे (इन
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.12293)
- **Original**: ज्वालासे शुद्ध किये गये हैं। वे मस्तकपर रत्रमय
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.12294)
- **Original**: # भ्रीकृष्णजन्मखण्ड + 741 %4%4#%$ 5 £ 4 $ 8 58% 144 46466 44 84 44 4 4 4 इंड4 ऊ कफ % अ 5455 44585 95 8 64 88 8854 44 44455 56 6 ह 66 मुकुट धारण करती हैं। उनकी आकृति बड़ी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.12295)
- **Original**: पुष्करमें पहले-पहल इस ब्रतका अनुष्ठान किया मनोहर है। श्रेष्ठ मणियोंके सारतत्त्वसे जटित
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.12296)
- **Original**: था। ब्रतकी समाप्तिके दिन कोटि सूर्योके समान रत्रमयी माला उनके कण्ठ एवं वक्षःस्थलको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.12297)
- **Original**: प्रकाशमान भगवती जगदम्बाने उसे साक्षात्‌ दर्शन उद्धासित किये रहती है। पारिजातके फूलोंकी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.12298)
- **Original**: दिया। देवीके साथ लाख योगिनियाँ भी थीं। मालाएँ गलेसे लेकर घुटनोंतक लटकी रहती हैं।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.12299)
- **Original**: वे परमेश्वरी सुवर्णनिर्मित रथपर बैठी थीं और उनकी कटिका निमप्नभाग अत्यन्त स्थूल और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.12300)
- **Original**: उनके प्रसन्नमुखपर मुस्कराहट फैल रही थी। कठोर है। वे स्तनों और नूतन यौवनके भारसे
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.12301)
- **Original**: उन्होंने संयमशीला बेदबतीसे कहा। कुछ-कुछ झुकी-सी रहती हैं। उनकी झाँकी
- **Translation**: 

---

