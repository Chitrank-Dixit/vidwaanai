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

### Verse 1 (Sama Ved 0.2621)
- **Original**: 1008.असाव्यंशुर्मदायाप्सु दक्षो गिरिष्ठा:। श्येनो न योनिमासदत्‌
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2622)
- **Original**: पर्वत शिखरों पर उपलब्ध होने वाला, आनन्दवर्द्धक सोमरस, जल में मिश्रित होकर बाज़ पक्षी की भाँति वेगपूर्वक पात्र में प्रविष्ठ होता है
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2623)
- **Original**: 1009.शुभ्रमन्धो देववातमप्सु धौत॑ नृभि: सुतम्‌ । स्वदन्ति गाव: पयोभि:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2624)
- **Original**: 2।। याजकों द्वारा अभिषुत, देवों के श्रेष्ठ आहार, जल मिश्रित, पवित्र सोमरस को गौएँ अपना दुग्ध मिलाकर अधिक स्वादिष्ट बना रही हैं
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2625)
- **Original**: 1010.आदीमश्व न हेतारमशूशुभनन्‍नमृताय । मधो रसं सधमादे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2626)
- **Original**: इसके उपरान्त, अश्व के समान स्फूर्तिदायक इस सोमरस को याजकगण अमरत्व प्राप्ति की कामना से यज्ञ-स्थल पर स्थापित करते हैं
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2627)
- **Original**: 1011.अभि थूुम्स॑ बृहद्यश इषस्पते दिदीहि देव देवयुम्‌ ।वि कोशं मध्यम युव
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2628)
- **Original**: वनस्पतियों के स्वामी हे सोमदेव ! देवताओं के द्वारा वांछित महान्‌ ऐश्वर्य आप हमें प्रदान करें आप यज्ञशाला (मध्य कोश) में श्रेष्ठ स्थान पर स्थिर रहें
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2629)
- **Original**: 1012.आ क्यस्व सुदक्ष चम्वो: सुतो विशां वहन विश्पति: । वृष्टि दिव: पवस्व रीतिमपो जिन्वन्‌ गविष्टये धिय:
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2630)
- **Original**: राजा की भाँति सबका पालन करने वाले, बुद्धिशाली हे सोमदेव ! याजकों की बुद्धियों को सम्मार्ग की ओर प्रेरित करते हुए, अन्तरिक्ष से बरसने वाले पर्जन्य-वर्षा को तरह नीचे के पात्र में स्थिर होने की कृपा करें
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2631)
- **Original**: 1013.प्राणाःशिशुर्महीनां हिन्वन्नृतस्य दीधितिम्‌ । विश्वा परि प्रिया भुवदश्॒ द्विता
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2632)
- **Original**: 6.8 सामवेद-सहिता जल से उत्पन्न होने वाले हे दिव्य सोम ! यज्ञ के प्रकाशक, प्राण रूप अपने रस को प्रेरित करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2633)
- **Original**: सर्वप्रिय ह॒वि को ग्रहण करते हुए पृथ्वी और अन्तरिक्ष को प्रकाशित करें
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2634)
- **Original**: 1014.उप त्रितस्थ पाष्यो3रभक्त यहुहा पदम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2635)
- **Original**: यज्ञस्य सप्त धामभिरथ प्रियम्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2636)
- **Original**: त्रित (महान) क्रषि की गुफा में चड्टान के समान, कठोर दो फलकों के मध्य से प्राप्त होने वाले सोमरस की ऋत्विजों ने गायत्री आदि सात छन्‍्दों से स्तुति की
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2637)
- **Original**: 1015.त्रीणि त्रितस्य धारया पृष्ठेष्वैरयद्रयिम्‌ । प्रिमीते अस्य योजना वि सुक्रतु:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2638)
- **Original**: ब्रित (तीन भुवनों) के तीनों सवनों (कालों) में व्याप्त हे दिव्य सोम ! अपनी रस की धारा से इद्रदेव को प्रेरित करें । श्रेष्ठ याजक उनका (इन्द्र का) उत्तम स्तोत्रों से गुणगान करते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2639)
- **Original**: 1016.पवस्व वाजसातये पवित्रे धारया सुतः । इन्द्राय सोम विष्णवे देवेभ्यो मधुमत्तर:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.2640)
- **Original**: रस रूप में निष्पन्न हे सोमदेव ! अपनी मधुर-पोषक धारा से इन्द्र तथा विष्णु आदि सभो देवताओं की तृप्ति के लिए पवित्र होकर आप सुपात्र में स्थिर हों
- **Translation**: 

---

