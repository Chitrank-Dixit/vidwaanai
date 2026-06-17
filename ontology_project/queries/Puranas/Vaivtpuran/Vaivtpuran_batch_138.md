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

### Verse 1 (Vaivtpuran 8.6320)
- **Original**: जाता है, उसी तरह तुझ सनातन अमूल्य रत्रकी 'फलदाता है, उसे देखिये। जो पुण्यका बीज,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.6321)
- **Original**: प्राप्तिसे मेरा मनोरथ पूर्ण हो गया। जैसे चिरकालसे महोत्सवस्वरूप, “'पुत' नामक नरकसे रक्षा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.6322)
- **Original**: प्रवासी हुए प्रियतमके घर लौटनेपर स्त्रीका मन करनेका कारण और भवसागरसे पार करनेवाला
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.6323)
- **Original**: पूर्णतया हर्षमग्र हो जाता है, वही दशा मेरे मनकी है, शीघ्र ही उस पुत्रके मुखका अवलोकन
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.6324)
- **Original**: भी हो रही है। वत्स! जैसे एक पुत्रवाली माता कीजिये; क्योंकि समस्त तीर्थोँमें स्नान तथा सम्पूर्ण
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.6325)
- **Original**: चिरकालसे बाहर गये हुए अपने इकलौते पुत्रको यज्ञॉमें दीक्षा-ग्रहणका पुण्य इस पुत्रदर्शकके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.6326)
- **Original**: आया हुआ देखकर परितृष्ट होती है, वैसे हो इस पुण्यकी सोलहवीं कलाकी समानता नहीं कर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.6327)
- **Original**: समय मैं भी संतुष्ट हो रही हूँ। जैसे मनुष्य सकता। सर्वस्व दान कर देनेसे जो पुण्य होता
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.6328)
- **Original**: चिरकालसे नष्ट हुए उत्तम रत्नको तथा अनावृष्टिके है तथा पृथ्वीकी प्रदक्षिणा करनेसे जिस पुण्यकी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.6329)
- **Original**: समय उत्तम वृष्टिको पाकर हर्षसे फूल उठता है, प्राप्ति होती है, वे सभी इस पुत्रदर्शन जन्य पुण्यके
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.6330)
- **Original**: उसी प्रकार तुझ पुत्रको पाकर मैं भी हर्ष-गद्गद सोलहवें अंशके भी बराबर नहीं हैं। हो रहो हूँ। जैसे चिरकालके पश्चात्‌ आश्रयहीन पार्वतीके ये वचन सुनकर शिवजीका मन
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.6331)
- **Original**: अंधेका मन परम निर्मल नेत्रकी प्राप्तिसे प्रसन्न हो हर्षमग्र हो गया। वे तुरंत ही अपनी प्रियतमाके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.6332)
- **Original**: जाता है, वही अवस्था (तुझे पाकर) मेरे मनकी साथ अपने घर आये। वहाँ उन्होंने शय्यापर अपने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.6333)
- **Original**: भी हो रही है। जैसे दुस्तर अगाध सागरमें गिरे पुत्रको देखा। उसकी कान्ति तपाये हुए स्वर्णके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.6334)
- **Original**: हुए अथवा विपत्तिमें फैसे हुए नौका आदि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.6335)
- **Original**: 316 * संक्षिप्त ब्रह्मवैवर्तपुराण « #48888 8888 4888 #8 88 498 98 # 4 ## 4 ## 58 # 458 # 944 # 8956 ## & # 55 5 554 4 8 5 5 $ 5 $ 14 55 84 18444 4 4 4 साधनविहीन मनुष्यका मन नौकाको पाकर आनन्दसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.6336)
- **Original**: चिरकालसे व्रतोपवास करनेवाले भूखे मनुष्योंका भर जाता है, बैसे ही मेरा मन भी आनन्दित हो
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.6337)
- **Original**: मन जैसे सामने उत्तम अन्न देखकर प्रसन्न हो रहा है। जैसे प्याससे सूखे हुए कण्ठवाले
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.6338)
- **Original**: उठता है, उसी तरह मेरा मन भी हर्षित हो रहा मनुष्योंका मन चिरकालके पश्चात्‌ अत्यन्त शीतल
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.6339)
- **Original**: है।' यों कहकर पार्वतीने अपने बालकको गोदमें एवं सुवासित जलको पाकर प्रसन्न हो जाता है,
- **Translation**: 

---

