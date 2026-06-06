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

### Verse 1 (Brahamand 0.501)
- **Original**: 60। नर-किन्नर-राक्षस-पक्षी-पश्चु-मृत और उरसों करा सृजन किया:करते हैं। अव्यय अथवा व्यय दोनों स्थावरों जंगसों का-सृजन-करते हैं
- **Translation**: 

---

### Verse 2 (Brahamand 0.502)
- **Original**: [ ब्रह्माण्ड पुराण तेषां ते यांति कर्माणि:प्रशक्‌ सृष्टानि स्वयंभुवा । तान्येव प्रतिपयंतें सृज्यमाना: पुनः पुनः:
- **Translation**: 

---

### Verse 3 (Brahamand 0.503)
- **Original**: 62 हिज्ाहिल मुदुक़ रे धर्माधमौं क़ृताकृते
- **Translation**: 

---

### Verse 4 (Brahamand 0.504)
- **Original**: तेषामेव पृथक्‌ सूतमविभक्त' ज््यं विदुः
- **Translation**: 

---

### Verse 5 (Brahamand 0.505)
- **Original**: 83 एतदेव॑ च नेबं चे न॑ चोभे नानुभे तथा
- **Translation**: 

---

### Verse 6 (Brahamand 0.506)
- **Original**: कर्म स्वविषयं प्राहु: सत्वस्था: समदर्शिनः
- **Translation**: 

---

### Verse 7 (Brahamand 0.507)
- **Original**: 64 नामात्मपञथ्चभूतानां कृतानां च प्रपथ्चताम्‌ । दिवणब्देन पञ्चेते निर्मने सः महेश्वर:
- **Translation**: 

---

### Verse 8 (Brahamand 0.508)
- **Original**: 65 आर्षाणि चेव नामानि याश्च देवेषु सृश्टय: । जवेर्या न प्रसूयन्ते पुनस्तेभ्यों दधत्प्रभु:
- **Translation**: 

---

### Verse 9 (Brahamand 0.509)
- **Original**: 8 6 इत्येवं कारणाइभूतों लोकसर्ग: स्वयंभ्ुवः । मह॒दाद्यां विशेषान्ता विकाराः: प्राकृता: स्वयम्‌
- **Translation**: 

---

### Verse 10 (Brahamand 0.510)
- **Original**: &7 अन्द्रसूय प्रभो लोको ग्रहनक्षेत्रंमण्डित: । नदीभिश्च समुद्रैश्च पर्वेतेएच सहस्नश:
- **Translation**: 

---

### Verse 11 (Brahamand 0.511)
- **Original**: & 8 ; वे'सबः उनके कर्मों को: प्राप्ततहोते हैं जिनका कि स्वयदम्भुने पूर्व में ही सृजन कर दिया था । बार-बार सृजन को प्राप्त होते हुए उन्हीं कर्मों -को प्रतिपन्‍त हुआ करते हैं
- **Translation**: 

---

### Verse 12 (Brahamand 0.512)
- **Original**: 62। हिल्न॒ और अहिसा वाले, भृदु और क्र, र-धर्म और अधर्म ओर कृत तथा अक्ृत उनके ही पृथक उत्पन्न हुए थे
- **Translation**: 

---

### Verse 13 (Brahamand 0.513)
- **Original**: यह अवि-- भक्त तीन जाते लीजिए ।63। यह इस प्रकार से है ओर इस श्रकार से नहीं: है-बोनों ही नहीं हैं और दोनों हैं । सत्व में स्थित समदर्शी अर्थात्‌ सबको एक ही समान देखने वाले अपने विषय को कर्म कहते हैं ।64। नामात्म पथ्च भूतों की और कुतों की प्रपठचता को बनाया था । उत्त महेश्वर ने दिन शब्द से ये ही पाँच हैं जिसका निर्माण किया था ।€5। देवों में जो सूष्टियाँ हैं और आंध नाम हैं शरवंरी में प्रसूत नहीं: होते हैं---फिर प्रभु ने उनके:लिए धारण किया था: ।€6
- **Translation**: 

---

### Verse 14 (Brahamand 0.514)
- **Original**: यह इसी रीति से स्वयम्भू का कारण से लोकों का सग्रें हुआ-था । महत्‌-जिनके आदि: मेँ होने वाला है तथा विशेष के अन्त पर्यन्त विक्रार स्वयं प्राकृत हैं ।67।:चन्द्रमाँ और सूर्य की प्रभा. वाला लोक जो'ग्रहों और नक्षत्रों से मण्डित है
- **Translation**: 

---

### Verse 15 (Brahamand 0.515)
- **Original**: जहाँ बहुत नदियाँ हैं--समुद्र है-और सहस्तों पव॑त हैं>इन सबसे मण्डित है ।65।
- **Translation**: 

---

### Verse 16 (Brahamand 0.516)
- **Original**: लीककल्पनम:(2) .-
- **Translation**: 

---

### Verse 17 (Brahamand 0.517)
- **Original**: [ 63 _ पुरेश्च विविध रम्ये: स्फीतैजैनपदेदस्तथा । _ ्द अस्मिच्‌ ब्रह्मवनेडव्यो ब्रह्मा चरति सर्वेवित्‌
- **Translation**: 

---

### Verse 18 (Brahamand 0.518)
- **Original**: 66 .... अव्यक्तबी जप्र भवस्तस्यैबानुग्रहे स्थित: । बुद्धिस्कन्ध मयश्चैव .इन्द्रियान्त रकोटर:
- **Translation**: 

---

### Verse 19 (Brahamand 0.519)
- **Original**: 1 00 महाभूत प्रका शश्च .विशेषे: प्रत्रवांस्तु सः । धर्माधर्म सुपुष्पस्तु सुखदुःखफलोदय:
- **Translation**: 

---

### Verse 20 (Brahamand 0.520)
- **Original**: 101 .. . - आजीव: सर्वेभूतानां ब्रह्मवृक्ष: सनातन: । का एतदबह्मवनं जैव ब्रह्मवृक्षस्य तस्य तत्‌
- **Translation**: 

---

