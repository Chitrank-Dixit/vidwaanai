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

### Verse 1 (Vaivtpuran 7.9833)
- **Original**: घिरा हुआ था। साक्षात्‌ विश्वकर्माने दिव्य प्रस्तरोंद्रार बलभद्र-दोनों तेरे काल हैं और इस समय
- **Translation**: 

---

### Verse 2 (Vaivtpuran 7.9834)
- **Original**: उसका निर्माण किया था। इन्द्रनील, मरकत और गोकुलके नन्दभवनमें पल रहे हैं।' पद्मराग मणियोंसे उस भव्य भवनकी बड़ी शोभा वह आकाशवाणी सुनकर राजा कंसका
- **Translation**: 

---

### Verse 3 (Vaivtpuran 7.9835)
- **Original**: हो रही थी। सोनेके दिव्य कलश और चित्रित मस्तक झुक गया। उसे सहसा बड़ी भारी चिन्ता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 7.9836)
- **Original**: शुभ्र शिखर उस नन्द-मन्दिरकी शोभा बढ़ाते थे। प्राप्त हुई। उसने अनमने होकर आहारको भी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 7.9837)
- **Original**: चार द्वारोंसे समलंकृत गगनचुम्बी परकोटे उस त्याग दिया और प्राणोंसे भी बढ़कर प्रेयसी बहिन
- **Translation**: 

---

### Verse 6 (Vaivtpuran 7.9838)
- **Original**: भवनके आभूषण थे। उसमें लोहेके किवाड़ लगे सती-साध्वी पूतनाकों बुलाकर उस नीतिज्ञ नरेशने
- **Translation**: 

---

### Verse 7 (Vaivtpuran 7.9839)
- **Original**: हुए थे। द्वारोंपर द्वारपाल पहरा दे रहे थे। बह परम भरी सभामें इस प्रकार कहा।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 7.9840)
- **Original**: सुन्दर एवं रमणीय भवन सुन्दरी गोपाड्भनाओंसे कंस बोला--पूतने ! मेंरे कार्यकी सिद्धिके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 7.9841)
- **Original**: आवेष्टित था। मोती, माणिक्य, पारसमणि तथा लिये गोकुलके नन्द-मन्दिरमें जाओ और अपने
- **Translation**: 

---

### Verse 10 (Vaivtpuran 7.9842)
- **Original**: रत्नादि वैभवोंसे भरे हुए उस भव्य भवनमें एक स्तनकों विषसे ओतप्रोत करके शीघ्र ही
- **Translation**: 

---

### Verse 11 (Vaivtpuran 7.9843)
- **Original**: सुवर्णमय पात्र और घट भारी संख्यामें दिखायी दे नन्दके नवजात शिशुके मुखमें दे दो। वत्से! तुम
- **Translation**: 

---

### Verse 12 (Vaivtpuran 7.9844)
- **Original**: रहे थे। करोड़ों गौएँ उस भवनके द्वारकी शोभा मनके समान वेगसे चलनेवाली मायाशास्त्रमें बढ़ा रही थीं। लाखों ऐसे गोपकिल्भूर वहाँ निपुण और योगिनी हो। अतः मायासे मानवी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 7.9845)
- **Original**: विद्यमान थे, जिनका भरण-पोषण नन्दभवनसे ही रूप धारण करके तुम वहाँ जाओ। सुप्रतिष्टे ! तुम होता धा। विभिन्न कार्योंमें लगी हुई सहस्रो दुर्वासासे महामन्त्रकी दीक्षा लेकर सर्वत्र जाने
- **Translation**: 

---

### Verse 14 (Vaivtpuran 7.9846)
- **Original**: दासियाँ उस भवनकी शोभा बढ़ा रही थीं। सुन्दरी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 7.9847)
- **Original**: + आरीकृष्णजन्मखण्ड है] डड3े #&कऋक्ककऋकफकऋक कक 4 ## 44668 #%#4####### ###%%#%ऋ कक ऋ्््क्ऋ्ऋऋऋझ# %% 4 ########5# पूतनाने अत्यन्त मनोहर वेष धारण करके मन्द
- **Translation**: 

---

### Verse 16 (Vaivtpuran 7.9848)
- **Original**: दिया। साथ ही बह बोली--'गोपसुन्दरि ! तुम्हारा मुस्कानकी छटा बिखेरते हुए नन्द-मन्दिरमें प्रवेश
- **Translation**: 

---

### Verse 17 (Vaivtpuran 7.9849)
- **Original**: यह सुन्दर बालक अत्यन्त अद्भुत है। यह गुणोंमें किया। उसे महलमें प्रवेश करती देख वहाँकी 85 87; गोपियोंने उसका बहुत आदर किया। वे सोचने
- **Translation**: 

---

### Verse 18 (Vaivtpuran 7.9850)
- **Original**: 64 झ लगीं--'ये कमलालया लक्ष्मी अथवा साक्षात्‌ दुर्गा
- **Translation**: 

---

### Verse 19 (Vaivtpuran 7.9851)
- **Original**: 55.2 ही तो नहीं हैं, जो साक्षात्‌ श्रीकृष्णका दर्शन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 7.9852)
- **Original**: करनेके लिये यहाँ पधारी हैं।' गोपियों 2 गोपोंने उसे प्रणाम किया और कुशल-समाचार /, 4
- **Translation**: 

---

