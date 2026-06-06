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

### Verse 1 (Vaivtpuran 66.5726)
- **Original**: महामारीरूपिणी भी तुम्हीं हो। तुम्हीं कालरात्रि, स्वरूप हैं। तुम निद्रा, दया और मनको प्रिय
- **Translation**: 

---

### Verse 2 (Vaivtpuran 66.5727)
- **Original**: महारात्रि तथा मोहिनी, मोहरात्रि हो; तुम मेरी लगनेवाली तृष्णा हो। क्षुधा, क्षमा, शान्ति, ईश्वरी,
- **Translation**: 

---

### Verse 3 (Vaivtpuran 66.5728)
- **Original**: दुर्लब्नय माया हो, जिसने सम्पूर्ण जगत्‌को मोहित कान्ति तथा शाश्वती सृष्टि भी तुम्हीं हो। तुम्हीं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 66.5729)
- **Original**: कर रखा है तथा जिससे मुग्ध हुआ विद्वान्‌ पुरुष श्रद्धा, पुष्टि, तन्द्रा, लज्जा, शोभा और दया हो।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 66.5730)
- **Original**: भी मोक्षमार्गको नहीं देख पाता। सत्पुरुषोंके यहाँ सम्पत्ति और दुष्टोंक घरमें विपत्ति .. इस प्रकार परमात्मा श्रीकृष्णद्वारा किये गये भी तुम्हीं हो। तुम्हीं पुण्यवानोंके लिये प्रीतिरूप
- **Translation**: 

---

### Verse 6 (Vaivtpuran 66.5731)
- **Original**: दुगके दुर्गम संकटनाशनस्तोत्रका जो पूजाकालमें हो, पापियोंके लिये कलहका अड्भुर हो तथा पाठ करता है, उसे मनोवाज्छित सिद्धि प्राप्त समस्त जीबॉकी कर्ममयी शक्ति भी सदा तुम्हीं होती है। हो। देवताओंको उनका पद प्रदान करनेवाली
- **Translation**: 

---

### Verse 7 (Vaivtpuran 66.5732)
- **Original**: जो नारी वन्ध्या, काकवन्ध्या, मृतवत्सा तथा तुम्हीं हो। धाता (ब्रह्मा)-का भी धारण-पोषण
- **Translation**: 

---

### Verse 8 (Vaivtpuran 66.5733)
- **Original**: दुर्भा है, वह भी एक वर्षतक इस स्तोत्रका करनेवाली दयामयी धात्री तुम्हीं हो। सम्पूर्ण श्रवण करके निश्चय ही उत्तम पुत्र प्राप्त कर लेती देवताओंके हितके लिये तुम्हीं समस्त असुरोंका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 66.5734)
- **Original**: है। जो पुरुष अत्यन्त घोर कारागारके भीतर दृढ़ विनाश करती हो
- **Translation**: 

---

### Verse 10 (Vaivtpuran 66.5735)
- **Original**: तुम योगनिद्रा हो। योग तुम्हारा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 66.5736)
- **Original**: बन्धनमें बँधा हुआ है, वह एक ही मासतक स्वरूप है। तुम योगियोंको योग प्रदान करनेवाली
- **Translation**: 

---

### Verse 12 (Vaivtpuran 66.5737)
- **Original**: इस स्तोत्रको सुन ले तो अवश्य ही बन्धनसे हो। सिद्धोंकी सिद्धि भी तुम्हीं हो। तुम सिद्धिदायिनी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 66.5738)
- **Original**: मुक्त हो जाता है। जो मनुष्य राजयक्ष्मा, गलित और सिद्धयोगिनी हो। ब्रह्माणी, माहेश्वरी, विष्णु-
- **Translation**: 

---

### Verse 14 (Vaivtpuran 66.5739)
- **Original**: कोढ़, महाभयंकर शूल और महान्‌ ज्वरसे ग्रस्त माया, वैष्णबी तथा भद्रदायिनी भद्रकाली भी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 66.5740)
- **Original**: है, वह एक वर्षतक इस स्तोत्रका श्रवण कर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 66.5741)
- **Original**: # प्रकृतिखण्ड * 293 64544 88 888 # 4 54 488 84 48 444 58 9 5 9 5 8 % 4 5 4 5 5 $ 5 $ 5 5 8 5 5 5 5 5 55 4 . 5 क/ 55 4 5 15 1%/ 464 44888 88 /8 # ले तो शीघ्र ही रोगसे छुटकारा पा जाता है।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 66.5742)
- **Original**: शिवके तुल्य हो गये। पुत्र, प्रजा और पत्नीके साथ भेद (कलह आदि) * 30 दुर्गायै स्वाहा' यह मन्त्र मेरे मस्तककी होनेपर यदि एक मासतक इस स्तोत्रकों सुने तो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 66.5743)
- **Original**: रक्षा करे। इस मन्त्रमें छ: अक्षर हैं। यह भक्तोंके इस संकटसे मुक्ति प्राप्त होती है, इसमें संशय
- **Translation**: 

---

### Verse 19 (Vaivtpuran 66.5744)
- **Original**: लिये कल्पवृक्षके समान है। मुने! इस मन्त्रको नहीं है। राजद्वार, श्मशान, विशाल वन तथा
- **Translation**: 

---

### Verse 20 (Vaivtpuran 66.5745)
- **Original**: ग्रहण करनेके विषयमें वेदोंमें किसी बातका रणक्षेत्रमें और हिंसक जन्तुके समीप भी इस
- **Translation**: 

---

