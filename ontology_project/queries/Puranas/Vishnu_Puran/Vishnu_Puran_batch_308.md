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

### Verse 1 (Vishnu Puran 0.6141)
- **Original**: ! तब देवता और असुरोंमें पुनः संग्राम छिड़ा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6142)
- **Original**: उसमें सम्मार्गविरोधी दैत्यगण देवताओंद्वारा मारे गये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6143)
- **Original**: हे द्विज ! पहले दैत्योंके पास जो स्वधर्मरूप कवच था उसीसे उनकी रक्षा हुई थी। अबकी यार उसके नष्ट हो जानेसे वे भी नष्ट हो गये
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6144)
- **Original**: हे मैत्रेय ! उस समयसे जो स्मेग मायामोहद्वास प्रयर्तित मार्गका अब॒लम्बन करनेवाले हुए। वे 'नप्न! कहल्वये क्योंकि उन्होंने बेदत्रयीरूप बख्नक्ये त्याग दिया था
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6145)
- **Original**: ब्हाचारी, गृहस्थ, लानप्रस्थ और संन्यासी--ये चार ही आश्रमी हैं। इनके अतिरिक्त पाँचवाँ आश्रमी और कोई नहीं है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6146)
- **Original**: है मैत्रेय! जो पुरुष गृहस्थाश्रमको छोड़नेके अनन्तर बानप्रस्थ या संन्यासी पहों होता बह पापी भी नग्म ही है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6147)
- **Original**: हे बिप्र ! सामर्ध्य रहते हुए भी जो बिहित कर्म नहीं करता वह उसी दिन पतित हो जाता है और उस एक दिन-रातमें ही उसके सम्पूर्ण नित्यकर्मोंका क्षय हो जाता है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6148)
- **Original**: है मैयेय ! आपत्तिकालकों छोड़कर और किसी समय एक पक्षतक नित्यकर्मका त्याग करनेबाला पुरुष महान्‌ प्रायक्षित्तसे हो शुद्ध हो सकता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6149)
- **Original**: जो पुरुष एक यर्षत्क नित्य-क्रिया नहीं करता उसपर दृष्टि पड़ जानेसे साधु पुरुषको सदा सूर्यका दर्दान करना चाहिये
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6150)
- **Original**: है महामते ! ऐसे पुरुषका स्पर्श होनेपर वस्वसहित खान करनेसे शुद्धि हो सकती है और उस पापात्माकी चुद्धि तो किसी भी प्रकार नहीं हो सकती
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6151)
- **Original**: जिस मनुष्यके घरसे देवगण, ऋषिगण, पितृगण और भूतगण बिना पूजित हुए निःश्वास छोड़ते अन्यत्र चले जाते हैं, स्मेकमें उससे बढ़कर और कोई पापी नहीं है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6152)
- **Original**: हे द्विज । ऐसे पुरुषके साथ एक वर्षतक सम्भाषण, कुझलप्रश्न और उठने -नैठनेसे मनुष्य उसीके समान पापात्मा हो जाता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6153)
- **Original**: जिसका शरीर अथवा गृह देखता आदिके निःधाससे निहत है उसके साथ अपने गृह, आसन और यर््र आदिको न मिलावे
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6154)
- **Original**: जो पुरुष उसके घरमें भोजन करता है, उसका आसन जेते चाप्येकशायने स सह्यास्तत्समो भवेत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6155)
- **Original**: म्रहण करता है अधवा उसके साथ एक ही झय्यापर दायन
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6156)
- **Original**: रस ्रीविध्यापुराण आआ#आ «18 22 देवतापितृभूतानि तथानभ्यर्च्य योउतिथीन्‌ । पुझक्ते स पातक भुद्दक्ते निष्कृतिस्तस्य नेष्यते
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6157)
- **Original**: 47 ब्राह्मणाद्यास्तु ये वर्णास्स्वधर्मादन्‍यतोमुखा: । यात्तति ते नप्नसंज्ञां तु हीनकर्मस्ववस्थिता:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6158)
- **Original**: 48 अतुर्णां यत्र वर्णानां मैत्रेयात्यन्तसड्ूरः । तत्रास्या साधुवृत्तीनामुपषघाताय जायते
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6159)
- **Original**: 49 अनभ्यर्चव्य ऋषीन्देबान्पितृभूताति्थीस्तथा । यो भुद्दक्ते तस्य सैंकलापात्पतन्ति नरके नरा:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6160)
- **Original**: 50 तस्मादेतान्नरों नप्मांखयीसन्त्यागदूषितान्‌ । सर्वदा वर्जयेत्राज्ञ आलापस्पर्शनादिषु । 51 श्रद्धावद्धि: कृतं यल्राहदेबान्पितृपितामहान्‌ । न प्रीणयति तच्छाद्धं यद्येभिरवक्लोकितम्‌
- **Translation**: 

---

