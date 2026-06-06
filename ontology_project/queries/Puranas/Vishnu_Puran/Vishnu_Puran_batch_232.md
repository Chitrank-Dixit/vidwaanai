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

### Verse 1 (Vishnu Puran 0.4621)
- **Original**: 36 तत: पुनः स बै देल्: प्राप्ते स्वारोचिषे5न्तरे । तुषितायां समुत्पन्नो हाजितस्तुषिति: सह
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4622)
- **Original**: 37 औत्तमेउ5प्यन्तरे देवस्तुषितस्तु पुनस्स वै। सत्यायामभवत्सत्य: सत्यैस्सह सुरोत्तम:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4623)
- **Original**: 38 तामसस्थान्तरे चैत्र सप्प्राप्ते पुनरेव हि। हर्यायां हरिभिस्सार्ध हरिरिव बभूव ह
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4624)
- **Original**: 39 रैवतेउप्यन्तरे देवस्सम्भूत्यां मानसो हरि: । सम्भूतो रैवतैस्सार्थ देवैर्देंववरो हरि:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4625)
- **Original**: 40 चाक्षुषे चान्तरे देवो वैकुण्ठ: पुरुषोत्तम: । विकुण्ठायामसौ जज्ञे बैकुण्ठैदैंवती: सह
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4626)
- **Original**: 41 मन्वन्तरेज सम्प्राप्ते तथा लैबस्वते ब्विज । वामन: कह्यपाद्धिष्णुरदित्यां सम्बभूत ह
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4627)
- **Original**: 42 ब्रिभिः क्रमैरिमॉल्लोकाजझित्वा येत महात्मना। पुरन्दराय ज्रैल्लेक्ये दत्ते निहतकण्टकम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4628)
- **Original**: 43 उस मन्वन्तरमें समेथा, विस्जा, हविष्मान्‌, उत्तम, मधु, अतिनामा और सहिष्णु--ये सात सप्तर्पि थे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4629)
- **Original**: तथा चाक्षुषके अति बलवान्‌ पुत्र ऊद, पूर और शतघुन्न आदि राज्याधिकारी थे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4630)
- **Original**: है विप्र ! इस समय इस सातवें मन्तन्तरमें सुर्यके पुत्र महातेजस्वी और बुड्धिमान्‌ श्राद्धदेवजी मनु हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4631)
- **Original**: ऐ सहासुने ! इस मन्वन्तरमें आदिस्य, यसु और रुदर आदि देवगण हैं तथा पुरन्दर नामक इन्द्र है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4632)
- **Original**: इस समय वसिष्ठ, काक्यप, अत्रि, जमदओ, गौतरा, विश्वामित्र और भरद्वाज--ये सात सप्तर्पि हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4633)
- **Original**: 32 । तथा वेजल्कत मनुके इक्ष्वाकु, नुग, धृष्ट, शर्याति, नरिष्यत्त, नाभाग, अरिष्ट, करूष और परथध--ये अत्यन्त लोकप्रसिद्ध और घर्मात्मा नौ पुत्र हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4634)
- **Original**: समस्त मन्‍्वन्तरोंमें देवरूपसे स्थित भगवान्‌ खिष्णुकों अनुपम और सत्वप्रधाना इक्ति ही संसारकी स्थिति उसकी अधिए्ठात्री होती है । 305
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4635)
- **Original**: सबसे पहले स्वायम्भुव-मन्वन्तरमें मानसटेव यज्ञपुरुष उस विष्णु- झक्तिके अदसे हो आकूतिके गर्भसे उत्पन्न हुए थे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4636)
- **Original**: फिर स्वारोशिष-सन्वन्तरके उपस्थित होनेपर वे सानसदेत श्रीअजित हो जुषित नामक देवगणोंके साथ त्तासे उत्पन्न हुए
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4637)
- **Original**: फिर उत्तम-मन्यन्तरमें खे तुप्तिदेव ही देवश्रेष्ठ सत्यगणके सहित सत्यरूपसे स्ल्याके उद्धरसे प्रकट हुए.
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4638)
- **Original**: तामस-मन्बन्तस्के प्राप्त होजेपर वे हरि नाम देवगणके सहित हरिरूपसे हर्याक्े गर्भसे उत्पन्न हुए
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4639)
- **Original**: तंत्पशात्‌ वे देवश्रेष्ट हरि, वैलत-मन्लक्षरपें तत्कालोन देवगणके सहित सम्भूतिके उदरसे प्रकट होकर मानस नामसे विख्यात हुए
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4640)
- **Original**: सथा याक्ष॒प-मन्वन्तरमें ले प्रुषोत्तम भगवान्‌ खैकुण्ठ नामक देबगणोंके सहित विकुण्ठासे-उत्पत्न होकर बैकुण्ठ कहलाये
- **Translation**: 

---

