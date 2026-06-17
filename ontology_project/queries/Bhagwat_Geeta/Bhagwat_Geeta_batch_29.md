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

### Verse 1 (Bhagwat_Geeta 7.724)
- **Original**: अव्यक्त व्यक्तिमापन्नं मन्यन्ते मामबुद्धय:ः । परं॑ भावमजानन्तो ममाव्ययमनुत्तमम्‌
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 7.725)
- **Original**: बुद्धिहीन पुरुष मेरे अनुत्तम अविनाशी परम भावको न जानते हुए मन-इन्द्रियोंसे परे मुझ सच्िदानन्दघन परमात्माको मनुष्यकी भाँति जन्मकर व्यक्तिभावको प्राप्त हुआ मानते हैं
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 7.726)
- **Original**: नाहं प्रकाश: सर्वस्य योगमायासमावृतः । मूढो5यं नाभिजानाति लोको मामजमव्ययम्‌
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 7.727)
- **Original**: अपनी योगमायासे छिपा हुआ मैं सबके प्रत्यक्ष नहीं होता, इसलिये यह अज्ञानी जनसमुदाय मुझ जन्मरहित अविनाशी परमेश्वरको नहीं जानता अर्थात्‌ मुझको जन्मने-मरनेवाला समझता है
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 7.728)
- **Original**: वेदाहं समतीतानि वर्तमानानि चार्जुन। भविष्याणि च भूतानि मां तु वेद न कश्चन
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 7.729)
- **Original**: हे अर्जुन ! पूर्वमें व्यतीत हुए और वर्तमानमें स्थित तथा आगे होनेवाले सब भूतोंको मैं जानता हूँ, परन्तु
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 7.730)
- **Original**: 106 * श्रीमद्धगवद्रीता * मुझको कोई भी श्रद्धा-भक्तिरहित पुरुष नहीं जानता
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 7.731)
- **Original**: इच्छाद्वेषसमुत्थेन. द्वन्द्रमोहेन॒ भारत। सर्वभूतानि सम्मोहं सर्गे यान्ति परन्तप
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 7.732)
- **Original**: हे भरतवंशी अर्जुन! संसारमें इच्छा और द्वेषसे उत्पन्न सुख-दुःखादि द्वन्द्ररूप मोहसे सम्पूर्ण प्राणी अत्यन्त अज्ञताको प्राप्त हो रहे हैं
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 7.733)
- **Original**: येषां त्वन्तगतं पापं जनानां पुण्यकर्मणाम्‌ । ते द्न्द्ठमोहनिर्मुक्ता भजन्ते मां दूढब्रता:
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 7.734)
- **Original**: परन्तु निष्कामभावसे श्रेष्ठ कर्मॉका आचरण करनेवाले जिन पुरुषोंका पाप नष्ट हो गया है, वे राग- द्वेषजनित द्न्द्ररूप मोहसे मुक्त दृढ़निश्चयी भक्त मुझको सब प्रकारसे भजते हैं
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 7.735)
- **Original**: जरामरणमोक्षाय मामाश्रित्य यतन्ति ये। ते ब्रह्म तद्विदुः कृत्स्त्रमध्यात्मं कर्म चारिलम्‌।
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 7.736)
- **Original**: जो मेरे शरण होकर जरा और मरणसे छूटनेके लिये यत्न करते हैं, वे पुरुष उस ब्रह्मको, सम्पूर्ण अध्यात्मको, सम्पूर्ण कर्मको जानते हैं
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 7.737)
- **Original**: साधिभूताधिदैवं मां साधियज्ञं च ये विदु: । प्रयाणकाले5पि च मां ते विदुर्युक्तचेतस:
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 7.738)
- **Original**: जो पुरुष अधिभूत और अधिदैवके सहित तथा अधियज्ञके सहित (सबका आत्मरूप) मुझे अन्तकालमें
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 7.1199)
- **Original**: 176 * श्रीमद्धगवद्रीता * पुरुष: प्रकृतिस्थो हि भुड्न्क्ते प्रकृतिजान्गुणान्‌। कारणं गुणसड्रो5स्थ सदसद्योनिजन्मसु
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 7.1200)
- **Original**: प्रकृतिमें' स्थित ही पुरुष प्रकृतिसे उत्पन्न त्रिगुणात्मक पदार्थोको भोगता है और इन गुणोंका संग ही इस जीवात्माके अच्छी-बुरी योनियोंमें जन्म लेनेका कारण है
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 7.1201)
- **Original**: उपद्रष्टानुमन्ता च भर्ता भोक्ता महेश्वरः । परमात्मेति चाप्युक्तो देहेउस्मिन्पुरुष: पर:
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 7.1202)
- **Original**: इस देहमें स्थित यह आत्मा वास्तवमें परमात्मा ही है। वह साक्षी होनेसे उपद्रष्ट और यथार्थ सम्मति देनेवाला होनेसे अनुमन्ता, सबका धारण-पोषण करनेवाला होनेसे भर्ता, जीवरूपसे भोक्ता, ब्रह्मा आदिका भी स्वामी होनेसे महेश्वर और शुद्ध सच्चिदानन्दघन होनेसे परमात्मा-- ऐसा कहा गया है
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 7.1203)
- **Original**: य एवं वेत्ति पुरुषं प्रकृतिं च गुणैः सह। सर्वथा वर्तमानोडउपि न स भूयो5भिजायते
- **Translation**: 

---

