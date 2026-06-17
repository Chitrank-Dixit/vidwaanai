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

### Verse 1 (Vaivtpuran 543.15254)
- **Original**: भाँति मिथ्या और मोहका ही कारण है। पाक्नभौतिक हैं; बही आज मेरी आँखोंके सामने है। आजके
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.15255)
- **Original**: शरीर एवं संसारके निर्माणका हेतु भी मिथ्या एवं बाद मुझ पातकीको तुम्हारे चरणारविन्दोंका दर्शन अनित्य है। माग्रासे ही मनुष्य इसे सत्य मान रहा कहाँ मिलेगा ? मेरा यह मलमूत्रधारी शरीर अपने है। वह समस्त कर्मोंमें काम, क्रोध, लोभ और कर्मबन्धनसे बँधा हुआ है। बेटा! अब ऐसा दिन
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.15256)
- **Original**: मोहसे वेष्टित है और मायासे सदा मोहित, कब प्राप्त होगा, जब कि ब्रह्मा आदि देवताओंके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.15257)
- **Original**: ज्ञानीीन एवं दुर्बल है। निद्रा, तन्द्रा, श्रुधा भी स्वामी तुमसे बातचीत करनेका शुभ अवसर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.15258)
- **Original**: पिपासा, क्षमा, श्रद्धा, दया, लज्जा, शान्ति, धृति मुझ-जैसे पापीकों सुलभ होगा ? महेश्वर! कृपानाथ !
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.15259)
- **Original**: पुष्टि और तुष्टि आदिसे भी वह आवृत है। जैसे मुझपर कृपा करों। मैंने अपना बेटा समझकर
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.15260)
- **Original**: वृक्ष काक आदि पक्षियोंका आश्रय है; उसी प्रकार तुम्हारे साथ जो दुर्नातिपूर्ण व्यवहार किया है;
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.15261)
- **Original**: मन, बुद्धि, चेतना, प्राण, ज्ञान और आत्मासहित मेरे उस अपराधको क्षमा कर दो। ब्रह्मा, शिव,
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.15262)
- **Original**: सम्पूर्ण देवता शरीरका आश्रय लेकर रहते हैं। मैं शेषनाग और मुनि भी तुम्हारे चरणारविन्दोंका
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.15263)
- **Original**: सर्वेश्वर ही पूर्ण ज्ञानस्वरूप आत्मा हूँ। ब्रह्मा मन चिन्तन करते हैं। सरस्वती और श्रुति भी तुम्हारी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.15264)
- **Original**: हैं, सनातनी प्रकृति बुद्धि हैं, प्राण विष्णु हैं तथा स्तुति करनेमें जडवत्‌ हो जाती हैं; फिर मेरी चेतना और उसको अधिप्नात्री देवी लक्ष्मी हैं। क्या बिसात है? शरीरमें मेरे रहनेसे हो सबकी स्थिति है। मेरे चले यों कहकर नन्दजी दुःख और शोकसे जानेपर वे भी सब-के-सब चले जाते हैं। हम व्याकुल हो गये। पुत्रवियोगसे विह्लल हो रोते-
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.15265)
- **Original**: सबके त्याग देनेपर शरीर तत्काल गिर जाता है; रोते उन्हें मूर्छा आ गयी। यह देख जगत्पति
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.15266)
- **Original**: इसमें संशय नहीं है। उसके पाँचों भूत उसी क्षण भगवान्‌ श्रीकृष्ण संत्रस्त हो उन्हें यत्रपूर्वक
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.15267)
- **Original**: समष्टिगत पाँचों भूतोंमें विलीन हो जाते हैं। नाम समझाने-बुझाने लगे। उन्होंने नन्दको परम उत्तम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.15268)
- **Original**: केवल संकेतरूप है। बह निष्फल और मोहका आध्यात्मिक ज्ञान प्रदान किया। कारण है। तात! अज्ञानियोंको ही शरीरके लिये श्रीभगवानने कहा--पिताजी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.15269)
- **Original**: लोकमें जितने
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.15270)
- **Original**: शोक होता है; ज्ञानियोंको किश्लिन्मात्र भी दुःख जन्मदाता पिता हैं, उन सबसमें तुम्हारा श्रेष्ठ स्थान
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.15271)
- **Original**: नहीं होता। निद्रा आदि जो शक्तियाँ हैं; वे सब है। सर्वश्रेष्ठ ब्रजेश्वर! होशमें आओ और उत्तम
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.15272)
- **Original**: प्रकृतिकी कलाएँ हैं। काम, क्रोध लोभ और कल्याणमय ज्ञान सुनो। यह श्रेष्ठ आध्यात्मिक ज्ञान
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.15273)
- **Original**: मोहके साथ जो पाँचवाँ अहंकार है; वे सब ज्ञानियोंके लिये भी परम दुर्लभ है। वेद-शास्त्रमें
- **Translation**: 

---

