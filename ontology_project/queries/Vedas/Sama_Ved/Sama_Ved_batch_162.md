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

### Verse 1 (Sama Ved 0.3221)
- **Original**: हे दिव्य सोम ! हमें अन्न और धन की प्राप्ति कराने हेतु आप वायुदेव को हैं।&24 करें । शोधित किये गये आप, मित्र और वरुण देवों को, मरुत्‌ की सामर्थ्य को, इन्द्रादि देवों को, आकाश और पृथ्वी के हर्ष को बढ़ाने वाले हों
- **Translation**: 

---

### Verse 2 (Sama Ved 0.3222)
- **Original**: [* क. स्वाध्यायमण्डल पारडी - नो' ख. वैदिक य्नालय अजमेर - 'ना' ग. आक्सफोर्ड यूनिवर्सिटी - पैक्सपूलर (1849) -*च] 1255. महत्तत्सोमो महिषश्चकारापां यद्गरभों5वृणीत देवान्‌ । अदधादिन्द्रे पवमान ओजो5जनयत्सूयें ज्योतिरिन्दु:
- **Translation**: 

---

### Verse 3 (Sama Ved 0.3223)
- **Original**: जल का गर्भरूप यह सोम देवताओं के सेवनार्थ प्रयुक्त होता है । संस्कारित हुए इस सोम ने इन्द्देव में बल भरा और सूर्यदेव में तेज स्थापन किया है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.3224)
- **Original**: 1256. एप देवो अमर्त्य: पर्णवीरिव दीयते । अभि द्रोणान्यासदम्‌
- **Translation**: 

---

### Verse 5 (Sama Ved 0.3225)
- **Original**: मरणघर्मरहित यह दिव्य सोम वेग से गतिमान्‌ पक्षी के सदृश, कलश में वेग से प्रविष्ट होता है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.3226)
- **Original**: 1257. एष विप्रैरभिष्टुतो5पो देवो वि गाहते । दधद्॒त्लानि दाशुषे
- **Translation**: 

---

### Verse 7 (Sama Ved 0.3227)
- **Original**: । श्रेष्ठ पु के द्वारा प्रशंसित होने वाला यह दिव्य सोम, हविदाता को धन प्रदान करता हुआ, जल में मिश्रित होता है.
- **Translation**: 

---

### Verse 8 (Sama Ved 0.3228)
- **Original**: 1258. एप विश्वानि वार्या शूरो यन्निव सत्वभि: । पवमान: सिषासति
- **Translation**: 

---

### Verse 9 (Sama Ved 0.3229)
- **Original**: यह शोधित, बलयुक्त सोम अपनी सामर्थ्य से उत्तम ऐश्वर्य को प्राप्त करते हुए, उसके समुचित वितरण की इच्छा करता है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.3230)
- **Original**: 10.2 सामवेद-संहिता 1259. एष देवो रथर्यति पवमानों दिशस्यति । आविष्कृणोति वग्वनुम्‌
- **Translation**: 

---

### Verse 11 (Sama Ved 0.3231)
- **Original**: यह शोधित दिव्य सोम ध्वनि करते हुए यज्ञ स्थल में जाने हेतु, उपयुक्त माध्यम की कामना करता है और याजकों को इष्ट पदार्थ प्रदान करने की इच्छा रखता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.3232)
- **Original**: 1260. एष देवो विपन्युभि: पवमान ऋतायुभिः । हरिरवाजाय मृज्यते
- **Translation**: 

---

### Verse 13 (Sama Ved 0.3233)
- **Original**: इस शोधित किये गये सोम को उद्‌गातागण स्तुतियों द्वारा उसी तरह विभूषित करते हैं, जिस प्रकार युद्धोन्‍्मुख अश्व को सब प्रकार से सज्जित किया जाता है
- **Translation**: 

---

### Verse 14 (Sama Ved 0.3234)
- **Original**: 1261. एप देवो विपा कृतो5ति ह्वरांसि धावति। पवमानों अदाभ्य:
- **Translation**: 

---

### Verse 15 (Sama Ved 0.3235)
- **Original**: अँगुलियों द्वारा निवोड़कर शोधित किया गया सोम, स्वयं अदम्य रहकर शत्रुओं का दमन करता है
- **Translation**: 

---

### Verse 16 (Sama Ved 0.3236)
- **Original**: 1262. एष दिवं वि धावति तिरो रजांसि धारया। पवमान: कनिक्रदत्‌
- **Translation**: 

---

### Verse 17 (Sama Ved 0.3237)
- **Original**: शोधित होकर शब्द करते हुए धार रूप में प्रकट सोम, शत्रुलोकों (प्रकृति चक्र में आने वाले अवरोधों) को जीतकर यज्ञ के प्रभाव से पुन: ऊर्ध्वगति पाता है
- **Translation**: 

---

### Verse 18 (Sama Ved 0.3238)
- **Original**: [यहाँ प्रकृति-चक्र (इकॉलाजिकल सर्किल) को जीवन्त बनाये रखने का संकेत है ।] 1263. एप दिवं व्यासरत्तिरो रजांस्यस्तृत:
- **Translation**: 

---

### Verse 19 (Sama Ved 0.3239)
- **Original**: पवमान: स्वध्वर:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3240)
- **Original**: उत्तम यज्ञकारक, शोधित दिव्य सोम, शत्रुओं को पराजित करने में समर्थ हुआ,-वह सोम इस बज्ञ स्थान से दिव्यलोक को गमन करता है
- **Translation**: 

---

