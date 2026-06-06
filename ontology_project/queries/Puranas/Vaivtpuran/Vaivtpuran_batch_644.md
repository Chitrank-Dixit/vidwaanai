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

### Verse 1 (Vaivtpuran 66.5746)
- **Original**: विचार नहीं किया गया है। मन्त्रकों ग्रहण स्तोत्रके पाठ और श्रवणसे मनुष्य संकटसे मुक्त
- **Translation**: 

---

### Verse 2 (Vaivtpuran 66.5747)
- **Original**: करनेमात्रसे मनुष्य विष्णुके समान हो जाता है। हो जाता है। यदि घरमें आग लगी हो, मनुष्य
- **Translation**: 

---

### Verse 3 (Vaivtpuran 66.5748)
- **Original**: दुर्गाय नमः' यह मन्त्र सदा मेरे मुखको दावानलसे घिर गया हो अथवा डाकुओंकी सेनामें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 66.5749)
- **Original**: रक्षा करे। '3 दुर्गे रक्ष" यह मन्त्र सदा मेरे फैंस गया हो तो इस स्तोत्रके श्रवणमात्रसे वह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 66.5750)
- **Original**: कण्ठकी रक्षा करे। ' 3» हीं श्रीं' यह मन्त्र निरन्तर उस संकटसे पार हो जाता है, इसमें कोई संदेह
- **Translation**: 

---

### Verse 6 (Vaivtpuran 66.5751)
- **Original**: मेरे कंधेका संरक्षण करे। '30 ड्डीं श्रीं क्लीं' नहीं है। जो महादरिद्र और मूर्ख है, वह भी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 66.5752)
- **Original**: यह मन्त्र सदा सब ओरसे मेरे पृष्ठठागका पालन एक वर्षतक इस स्तोत्रको पढ़े तो निस्संदेह विद्वान्‌
- **Translation**: 

---

### Verse 8 (Vaivtpuran 66.5753)
- **Original**: करे। 'हीं' मेरे वक्ष:स्थलकी और 'श्रीं' सदा और धनवान्‌ हो जाता है। मेरे हाथकी रक्षा करे। '30 श्रीं हीं क्लीं' यह नारदजीने कहा--समस्त धर्मोंके ज्ञाता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 66.5754)
- **Original**: मन्त्र सोते और जागते समय सदा मेरे सर्वाद्ञका तथा सम्पूर्ण ज्ञाममें विशारद भगवन्‌! ब्रह्माण्ड-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 66.5755)
- **Original**: संरक्षण करे। पूर्वदिशामें प्रकृति मेरी रक्षा करे। मोहन नामक प्रकृतिकवचका वर्णन कीजिये।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 66.5756)
- **Original**: अग्रिकोणमें चण्डिका रक्षा करे। दक्षिणदिशामें भगवान्‌ नारायण बोले--वत्स ! सुनो। मैं
- **Translation**: 

---

### Verse 12 (Vaivtpuran 66.5757)
- **Original**: भद्रकाली, नैत्यकोणमें महेश्वरी, पश्चिमदिशामें उस परम दुर्लभ कवचका वर्णन करता हूँ।
- **Translation**: 

---

### Verse 13 (Vaivtpuran 66.5758)
- **Original**: बाराही और वायव्यकोणमें सर्वमज्जला मेरा पूर्वकालमें साक्षात्‌ श्रीकृष्णने ही ब्रह्माजीको इस
- **Translation**: 

---

### Verse 14 (Vaivtpuran 66.5759)
- **Original**: संरक्षण करे। उत्तरदिशामें बैष्णवी, ईशानकोणमें कवचका उपदेश दिया था। फिर ब्रह्माजीने
- **Translation**: 

---

### Verse 15 (Vaivtpuran 66.5760)
- **Original**: शिवप्रिया तथा जल, थल और आकाशमें गड्जाजीके तटपर धर्मके प्रति इस सम्पूर्ण कबचका
- **Translation**: 

---

### Verse 16 (Vaivtpuran 66.5761)
- **Original**: जगदम्बिका मेरा पालन करे। वर्णन किया था। फिर धर्मने पुष्करतीर्थमें मुझे वत्स! यह परम दुर्लभ कबच मैंने तुमसे कृपापूर्वक इसका उपदेश दिया, यह वहीं कबच
- **Translation**: 

---

### Verse 17 (Vaivtpuran 66.5762)
- **Original**: कहा है। इसका उपदेश हर एकको नहीं देना है, जिसे पूर्वकालमें धारण करके त्रिपुरारि शिवने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 66.5763)
- **Original**: चाहिये और न किसीके सामने इसका प्रवचन त्रिपुरासुरका वध किया था और ब्रह्माजीने जिसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 66.5764)
- **Original**: ही करना चाहिये। जो वस्त्र, आभूषण और धारण करके मधु और कैटभसे प्राप्त होनेवाले
- **Translation**: 

---

### Verse 20 (Vaivtpuran 66.5765)
- **Original**: चन्दससे गुरुकी विधिवत्‌ पूजा करके इस भयको त्याग दिया था। जिसे धारण करके
- **Translation**: 

---

