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

### Verse 1 (Vaivtpuran 22.3842)
- **Original**: भगवती सावित्रीके दर्शन तो नहीं हुए, किंतु इनका पूजन किया। इसके बाद भारतवर्षमें राजा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 22.3843)
- **Original**: उनका प्रत्यादेश (उत्तर) प्राप्त हुआ। महाराज अश्वपतिने पहले इनकी उपासना कौ। तदनन्तर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 22.3844)
- **Original**: अश्वपतिको यह आकाशवाणी सुनायी दी--' राजन! चारों बर्णोके लोग इनकी आराधनामें संलग्न
- **Translation**: 

---

### Verse 4 (Vaivtpuran 22.3845)
- **Original**: तुम दस लाख गायत्रीका जप करो।' इतनेमें ही हो गये। वहाँ मुनिवर पराशरजी पधार गये। राजाने मुनिको नारदजीने पूछा--ब्रह्मन्‌! राजा अश्वपति
- **Translation**: 

---

### Verse 5 (Vaivtpuran 22.3846)
- **Original**: प्रणाम किया। मुनि राजासे कहने लगे। कौन थे ? किस कामनासे उन्होंने सावित्रीकी पूजा). पराशरने कहा--राजन्‌! गायत्रीका एक की थी? बारका जप दिनके पापको नष्ट कर देता है। दस भगवान्‌ नारायण बोले--मुने! महाराज
- **Translation**: 

---

### Verse 6 (Vaivtpuran 22.3847)
- **Original**: बार जप करनेसे दिन और रातके सम्पूर्ण पाप नष्ट अश्वपति मद्रदेशके नरेश थे। शत्रुओंकी शक्ति नष्ट
- **Translation**: 

---

### Verse 7 (Vaivtpuran 22.3848)
- **Original**: हो जाते हैं। सौ बार जप करनेसे महीनोंका करना और मित्रोंके कष्टका निवारण करना उनका
- **Translation**: 

---

### Verse 8 (Vaivtpuran 22.3849)
- **Original**: उपार्जित पाप नहीं ठहर सकता। एक हजारके स्वभाव था। उनकी रानीका नाम मालती था।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 22.3850)
- **Original**: जपसे वर्षोके पाप भस्म हो जाते हैं। गायत्रीके एक धर्मोंका पालन करनेवाली वह महाराज्ञी राजाके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 22.3851)
- **Original**: लाख जपमें एक जन्मके तथा दस लाख जपमें साथ इस प्रकार शोभा पाती थी, जैसे लक्ष्मीजी तीन जन्मोंके भी पापोंको नष्ट करनेकी अमोघ शक्ति भगवान्‌ विष्णुके साथ। नारद! उस महासाध्यी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 22.3852)
- **Original**: है। एक करोड़ जप करनेपर सम्पूर्ण जन्मोंके पाप नष्ट रानीने वसिष्टजीके उपदेशसे भक्तिपूर्वक भगवती
- **Translation**: 

---

### Verse 12 (Vaivtpuran 22.3853)
- **Original**: हो जाते हैं। दस करोड़ गायत्री-जप ब्राह्मणोंको *तुलसीं पुष्पसारां च॒ सर्ती पूर्ण्या मनोहरापू । कृत्छ्रपापेध्यदाहाय ज्वलदग्रिशिखोपमाम्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 22.3854)
- **Original**: युष्पेषु. तुलनापष्यस्था नासीद्‌ देवीषु वा मुने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 22.3855)
- **Original**: पवित्नरूपा सर्वासु तुलसी सा च कोीतिता
- **Translation**: 

---

### Verse 15 (Vaivtpuran 22.3856)
- **Original**: शिरोधायाँ च सर्वेषामीप्सितां विश्वपावनीमू। जीवन्सुक्तां मुक्तिदां च भजे तां हरिभक्तिदाम्‌
- **Translation**: 

---

### Verse 16 (Vaivtpuran 22.3857)
- **Original**: ( प्रकृतिखण्ड 22
- **Translation**: 

---

### Verse 17 (Vaivtpuran 22.3858)
- **Original**: 42--44)
- **Translation**: 

---

### Verse 18 (Vaivtpuran 22.6916)
- **Original**: + गणपतिखेण्डर 337 52 जन 4 464440404]0
- **Translation**: 

---

### Verse 19 (Vaivtpuran 22.6917)
- **Original**: ]]/// करनेपर भी मन्त्र सिद्धिदायक नहीं होता*।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 22.6918)
- **Original**: ध्यान करके भक्तिपूर्वक उन्हें षोडशोपचार समर्पित नारायण कहते हैं--महामुने ! यों जगदीश्वर
- **Translation**: 

---

