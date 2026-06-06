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

### Verse 1 (Vishnu Puran 0.5841)
- **Original**: अतः श्राद्धके प्रथम दिन पहले तो उपरोक्त गुणविद्िष्ट द्विजश्रेष्टॉंको निमन्त्रित करें और यदि उस दिन कोई अनिमन्ल्ित तपस्वी ब्राह्मण घर आ जायें तो उन्हें भो भोजन कराते
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.5842)
- **Original**: घर आये हुए ब्राह्मणोंका पहले पाद-शुद्धि आदिसे सल्कार करें; फिर हाथ घोकर उन्हें आचमन करानेके अनन्तर आसनपर ब्रिखवे। अपनी सामर्थ्यानुसार पिठतृगणके ल्त्ये अयुष्प और देवगणके र्छये युग्म ब्राह्मण नियुक्त करे अथवा दोनों पक्षोक्ति छिये एक-एक ज्राह्मणकी ही नियुक्ति करें
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.5843)
- **Original**: 13--15
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.5844)
- **Original**: और इसी प्रकार वैश्वदेवके सहित मातामह-श्राद्ध करे अथवा पितृपक्ष और मातामह-पक्ष दोनोंके लिये भक्तिपूर्वक एक ही वैश्वदेव- श्राद्ध करे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.5845)
- **Original**: देव-पक्षके ब्राह्मणोंको पूर्वाभिमुख बिठाकर और पितृ-पक्ष तथा मात्तामच-पक्षके ब्राह्मणोंको उत्तर-मुख्त बिझकर भोजन कराबे
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.5846)
- **Original**: है नूप ! कोई तो पितृ-पक्ष और मातामह-पक्षके श्राद्धोंको अलूग- अलग करनेके लिये कहते हैं और कोई महर्षि दोनोंका एक साथ एक पाक में हो अनुष्ठान करनेके पक्षमें हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.5847)
- **Original**: विज्ञ व्यक्ति प्रथम निमन्लित ब्राह्मणोंके बैठनेके लिये कुशा न्रिछाकर फिर अर्घ्यददान आदिसे विधिपूर्वक पूजा कर उनकी अनुमतिसे देवताओंका आवाहन करें
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.5848)
- **Original**: तदनन्तर श्राद्धविधिको जाननेबाला पुरुष यब-मिश्रित जलसे देवताओंक्व अर्ध्यदान करे और उन्हें विधिपूर्यक धूप, दीप, गन्ध तथा माल्य्र आदि निवेदन करे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.5849)
- **Original**: ये समस्त उपचार पितृगणके रिप्ये अपसव्य भावसे * निवेदन करे; और फिर ब्राह्मणोंकी अनुमतिसे दो भागोंमें खैटे हुए कुझाओंका दान करके मच्ोच्ारणपूर्वक पितृगणका आवाहन करे, तथा हे राजन्‌ ! अपसब्य- भावसे तिल््रेदकसे अर््यादि दे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.5850)
- **Original**: हे नृप ! उस समय यदि कोई भूखा पथिक अतिथि-
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.5851)
- **Original**: अ" 15 ] तुतीय अंदा 111 योगिनो विविधै रूपैनराणामुपकारिण: । भ्रमन्ति पृथित्रीमेतामविज्ञातस्वरूपिण:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.5852)
- **Original**: 24 दाग श्राद्धकालेउतिथिं बुध: । अ्राद्धक्रियाफल हन्ति नरेन्द्रापूजितो5तिथि:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.5853)
- **Original**: 25 जुह॒यादव्यक्षनक्षारवर्जमन्न॑ ततोउनले । अनुज्ञातो द्विजैस्तैस्तु त्रिकृत्वः पुरुषर्षभ:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.5854)
- **Original**: 26 अम्मये कव्यबाहाय स्वाहेत्यादौ नृपाहुतिः । सोमाय जै पितृमते दातव्या तदनन्तरम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.5855)
- **Original**: 27 वैवस्वताय चैवान्या तृतीया दीयते ततः । हुताबशिष्टमल्पान्न॑ विप्रपात्रेषु निर्वषषेत्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.5856)
- **Original**: 28 ततो5ज॑ मृष्टमत्यर्थभभीष्टमतिसंस्कृतम्‌ । दक्त्पवा जुषध्वमिच्छातो वाच्यमेतदनिष्ठुरम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.5857)
- **Original**: 29 भोक्तव्यं तैक्ष तबचित्तेमौनिभिस्सुमुखैः सुखम्‌। अक्कुद्धयता चात्वरता देय॑ तेनापि भक्तित:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.5858)
- **Original**: 30 रक्षोप्नमनत्रपटनं. भूमेरास्तरणं. तिल: । कृत्वा ध्येयास्स्वपितरस्त एवं ट्विजसत्तमा:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.5859)
- **Original**: 39 पिता प्रितामहश्ैव तथैव प्रपितामह: । मम तृप्ति प्रयान्वच्य विप्रदेहेषु संस्थिता:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.5860)
- **Original**: 32 पिता पितामहश्लैव तथैत प्रपितामहः । मम तृप्ति प्रयान्वद्य होमाप्यायितमूर्तवः
- **Translation**: 

---

