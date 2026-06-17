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

### Verse 1 (Vaivtpuran 543.15134)
- **Original**: प्रिय हैं, जो सृष्टि, पालन और संहार करनेवाली स्वर्गमें निवास करता है। सहस््र शिवलिड्रोंके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15135)
- **Original**: आद्या नागयणी शक्ति है, जिसके द्वारा मैं सृष्टि पूजनसे मनुष्यको मनोवाज्छित फलकी प्राप्ति होती
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15136)
- **Original**: करता हूँ, जिससे ब्रह्मा आदि देवता उत्पन्न होते है और जिसने एक लाख शिवलिजड्रोंकी पूजा कर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15137)
- **Original**: हैं, जिसका आश्रय लेनेसे जगत्‌ विजयी होता है, ली है, वह निश्चय ही शिवत्वको प्राप्त होता है। जिससे सृष्टि चलती है और जिसके बिना जो ब्राह्मण शिवलिड्लकी पूजा करता है, वह
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15138)
- **Original**: संसारका अस्तित्व ही नहीं रह सकता; वह जीवन्मुक्त होता है और जो शिवपूजासे रहित है, शक्ति मैंने शिबको अर्पित की है।* वह ब्राह्मण नरकगामी होता है। जो मनुष्य मेरेद्वारा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15139)
- **Original**: (अध्याय 74-75) हा 02 न जिनके दर्शनसे पुण्यलाभ और जिनके अनुष्टानसे पुनर्जन्मका निवारण होता है, उन वस्तुओं और सत्कर्मोंका वर्णन तथा विविध दानोंके पुण्यफलका कथन श्रीनन्दने कहा--सर्वेश्वर! जिनके दर्शनसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15140)
- **Original**: मोर, नौलकण्ठ, शड्खपक्षी, बछड़ेसहित गाय, पुण्य और जिन्हें देखनेसे पाप होता है, उन पीपलवृक्ष, पति-पुत्रवाली नारी, तीर्थयात्री मनुष्य, सबका परिचय दो। यह सुननेके लिये मेरे मनमें
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15141)
- **Original**: शा मम सन सुवर्ण, मणि, मोती, हीरा, माणिक्य, बड़ा कौतूहल है। तुलसी, श्रेत पुष्प, फल, श्वेत धान्य, घी, दही, श्रीभगवान्‌ बोले--तात! उत्तम ब्राह्मण,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15142)
- **Original**: मधु, भरा हुआ घड़ा, लावा, दर्पण, जल, श्वेत तीर्थ, वैष्णव, देवप्रतिमा, सूर्यदेव, सती स्त्री,
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15143)
- **Original**: पुष्पॉकी माला, गोरोचन, कपूर, चाँदी, तालाब, संन्यासी, यति, ब्रह्मचारी, गौ, अग्नि, गुरु, गजराज,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15144)
- **Original**: फूलोंसे भरी हुई वाटिका, शुक्लपक्षके चढद्नमा, सिंह, श्वेत अश्च, शुक, कोकिल, खज्जरीट, हंस,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15145)
- **Original**: अमृत, चन्दन, कस्तूरी, कुछ्लूम, पताका, अक्षयवर, * महादेव महादेव महादेवेतिवादिन:। पथ्चाद्‌ यामि च संत्रस्तो नामश्रवणलोभत:
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15146)
- **Original**: मनो में भक्तमूलं च प्राणा राधात्मिका ध्रुवम्‌। आत्मा में शंकरस्थानं शिव: प्राणाधिकश्न में
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15147)
- **Original**: आद्या नारायणी शक्ति: सृष्टिस्थित्यनतकारिणो
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15148)
- **Original**: करोपि थे यया सुष्टिं यया ब्रह्मादिदेवता:
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15149)
- **Original**: यया जयति विश्व च यया सुष्टि: प्रजायते । यया विना जगन्नास्ति मया दत्ता शिवाय चा
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15150)
- **Original**: (75। 89-92)
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15151)
- **Original**: + श्रीकृष्णजन्मखण्ड * 657 %ऋ###$#$####%##%##%%$%%
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15152)
- **Original**: ऋऋऊऋऋऋशऋ$ऊ कक ऋ %ऋऋऋफऋऋ फ
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15153)
- **Original**: #ऋ# ### 444 कक देववृक्ष, देवालय, देवसम्बन्धी जलाशय, देवताके
- **Translation**: 

---

