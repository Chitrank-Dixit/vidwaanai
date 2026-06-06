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

### Verse 1 (Vaivtpuran 55.5265)
- **Original**: यज्ञके फलका भागी होता है। यदि नारी इस जो मनुष्य श्रीकृष्णद्वारा किये गये इस राधास्तोत्रका
- **Translation**: 

---

### Verse 2 (Vaivtpuran 55.5266)
- **Original**: स्तोत्रका श्रवण करें तो वह पतिके सौभाग्यसे पाठ करता है, वह श्रीकृष्णमी भक्ति और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 55.5267)
- **Original**: सम्पन्न होती है। जो भक्तिपूर्वक इस स्तोत्रकों दास्यभाव प्राप्त कर लेता है, इसमें संशय नहीं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 55.5268)
- **Original**: सुनता है, वह निश्चय ही बन्धनसे मुक्त हो जाता है। स्त्रीसे वियोग होनेपर जो पवित्रभावसे एक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 55.5269)
- **Original**: है। जो प्रतिदिन भक्तिभावसे श्रीराधाकी पूजा मासतक इस स्तोत्रका श्रवण करता है, वह शीघ्र
- **Translation**: 

---

### Verse 6 (Vaivtpuran 55.5270)
- **Original**: करके प्रेमपूर्वक इस स्तोत्रका पाठ करता है, ही सती, सुन्दरी और सुशीला स्त्रीकों प्रात कर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 55.5271)
- **Original**: बह भवबन्धनसे मुक्त हो गोलोकधाममें लेता है। जो भार्या और सौभाग्यसे हीन है, वह
- **Translation**: 

---

### Verse 8 (Vaivtpuran 55.5272)
- **Original**: जाता है। (अध्याय 55) # 38-50“ 9#22695.5050050 श्रीजगन्मड्रल-राधाकबच तथा उसकी महिमा श्रीपार्वती बोलीं-- श्रीरधाकी पूजाका विधान
- **Translation**: 

---

### Verse 9 (Vaivtpuran 55.5273)
- **Original**: इस अति गोपनीय परम तत्त्वरूप तथा और स्तोत्र अत्यन्त अद्भुत है, उसे मैंने सुन
- **Translation**: 

---

### Verse 10 (Vaivtpuran 55.5274)
- **Original**: सर्वमन्त्रसमूहमय कवचका मुझसे वर्णन किया लिया। अब राधाकवचका वर्णन कौजिये। आपकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 55.5275)
- **Original**: था। यह वही कवच है, जिसे धारण करके पाठ कृपासे उसे भी सुनूँगी। करनेसे ब्रह्माने वेदमाता सावित्रीको पत्नीरूपमें प्राप्त श्रीमहेश्वने कहा--दुर्गें! सुनो। मैं परम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 55.5276)
- **Original**: किया। सुरेधरि! तुम सर्वलोकजननी हो। मुझे अद्भुत राधाकवचका वर्णन आरम्भ करता हूँ।! तुम्हारा स्वामी होनेका जो सौभाग्य प्राप्त हुआ पूर्वकालमें साक्षात्‌ परमात्मा श्रीकृष्णने गोलोकमें
- **Translation**: 

---

### Verse 13 (Vaivtpuran 55.5277)
- **Original**: है, वह इस कबचकों धारण करनेका ही प्रभाव
- **Translation**: 

---

### Verse 14 (Vaivtpuran 55.5278)
- **Original**: 276 * संक्षिप्त ब्रह्मवैवर्तपुराण « %4#%#%#### 5 # &# # ## # 44 ###& 868 6 #### 4 4 6 # % 5 4 % 44 4 4 45 ऋ% कऊ 4 ऋ हक कक ऋ कक ऋऊ कक
- **Translation**: 

---

### Verse 15 (Vaivtpuran 55.5279)
- **Original**: 46 44 4688 % है। इसीको धारण करके भगवान्‌ नारायणने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 55.5280)
- **Original**: और यम शासक हुए हैं। इसीका आश्रय लेनेसे महालक्ष्मीको प्राप्त किया। इसीको धारण करनेसे [काल एवं कालाग्रिरुद्र तीनों लोकॉंका संहार प्रकृतिसे परवर्ती निर्मुण परमात्मा श्रीकृष्ण पूर्वकालमें
- **Translation**: 

---

### Verse 17 (Vaivtpuran 55.5281)
- **Original**: करनेमें समर्थ हो सके हैं। इसीकों धारण करके सृष्टिरचना करनेकी शक्तिसे सम्पन्न हुए। जगत्पालक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 55.5282)
- **Original**: गौतम सिद्ध हुए, कश्यप प्रजापतिके पदपर विष्णुने इसीको धारण करके सिन्धुकन्याको प्राप्त
- **Translation**: 

---

### Verse 19 (Vaivtpuran 55.5283)
- **Original**: प्रतिष्ठित हो सके और मुनिवर दुर्वासाने अपनी किया। इसी कवचके प्रभावसे शेषनाग समस्त
- **Translation**: 

---

### Verse 20 (Vaivtpuran 55.5284)
- **Original**: पत्नीका वियोग होनेपर पूर्वकालमें देवीकी कलास्वरूपा ब्रह्माण्डको अपने मस्तकपर सरसोंके दानेकी
- **Translation**: 

---

