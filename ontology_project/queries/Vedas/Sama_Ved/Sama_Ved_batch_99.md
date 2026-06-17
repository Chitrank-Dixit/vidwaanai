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

### Verse 1 (Sama Ved 0.1961)
- **Original**: तेजस्वी, सभी इच्छाओं की पूर्ति करने वाले, ज्ञानवर्द्ध इस सोमरस को उसके शाश्वत स्वरूप का स्मरण करते हुए, विद्वानों ने तैयार किया है
- **Translation**: 

---

### Verse 2 (Sama Ved 0.1962)
- **Original**: 756.अय॑ सूर्य इबोपदूगयं सरांसि धावति। सप्त प्रवत आ दिवम्‌
- **Translation**: 

---

### Verse 3 (Sama Ved 0.1963)
- **Original**: देवलोक तक सप्तधाराओं ( सप्तकिरणों के रूप) में प्रवाहित, सूर्यदेव के समान सभी लोकों का द्रष्टा, यह सोम जल-पात्रों में शोध्ित किया जाता है
- **Translation**: 

---

### Verse 4 (Sama Ved 0.1964)
- **Original**: 2.6 सापवेद-संहिता 757.अयं॑ विश्वानि तिष्ठति पुनानो भुवनोपरि । सोमो देवो न सूर्य:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.1965)
- **Original**: पवित्र होने वाला यह सोमरस, सूर्यदेव के समान सभी लोकों में प्रकाशित होता है
- **Translation**: 

---

### Verse 6 (Sama Ved 0.1966)
- **Original**: 758.एपष प्रत्नेन जन्मना देवो देवे भ्य: सुतः । हरि: पवित्रे अर्धघति
- **Translation**: 

---

### Verse 7 (Sama Ved 0.1967)
- **Original**: सनातन रौति से संस्कारित किया गया यह हरिताभ सोमरस, देवों के लिए छलनी से छानकर शोधित किया जाता है
- **Translation**: 

---

### Verse 8 (Sama Ved 0.1968)
- **Original**: 759, एप प्रत्नेन मन्मना देवो देवेभ्यस्परि । कविर्विप्रेण वावृधे
- **Translation**: 

---

### Verse 9 (Sama Ved 0.1969)
- **Original**: सनातन स्तुतियों की सहायता से यह देदीप्यमान, ज्ञानी सोम ब्रद्मवेत्ताओं द्वारा देवगणों के लिए प्रकाशित किया जाता है
- **Translation**: 

---

### Verse 10 (Sama Ved 0.1970)
- **Original**: 760.दुहान: प्रलममित्पय: पवित्रे परि घिच्यसे । क्रन्दं देवाँ अजीजन:
- **Translation**: 

---

### Verse 11 (Sama Ved 0.1971)
- **Original**: बर्तन में निचोड़ा गया यह सोमरस छलनी में छाना जाता है । शब्दायमान यह सोम देवगणों को यज्ञ में आवाहित करता प्रतीत होता है
- **Translation**: 

---

### Verse 12 (Sama Ved 0.1972)
- **Original**: 761.उप शिक्षापतस्थुषो भियसमा धेष्टि शत्रवे । पवमान विदा रयिम्‌
- **Translation**: 

---

### Verse 13 (Sama Ved 0.1973)
- **Original**: हे सोमदेव ! अहितकारियों को भयभीत करके, आप अपने पास बैठने वालों को सन्मार्ग दिखाएँ और धन-धान्य से पूर्ण करें ।7
- **Translation**: 

---

### Verse 14 (Sama Ved 0.1974)
- **Original**: 762.उपो घु जातमप्तुरं गोभिर्भड्ं परिष्कृतम्‌
- **Translation**: 

---

### Verse 15 (Sama Ved 0.1975)
- **Original**: इन्दुं देवा अयासिषु:
- **Translation**: 

---

### Verse 16 (Sama Ved 0.1976)
- **Original**: निकालने के बाद सोमरस को जल में मिलाया जाता है । इस शत्रुनाशक, गाय के दूध से मिले सोमरस का आवाहन देवगण भी करते हैं
- **Translation**: 

---

### Verse 17 (Sama Ved 0.1977)
- **Original**: 763.उपास्मै गायता नर: पवमानायेन्दवे । अभि देवाँ इयक्षते
- **Translation**: 

---

### Verse 18 (Sama Ved 0.1978)
- **Original**: हे क्ग्रत्विजो ! देवगणों की प्रार्थना (इच्छा) करने की अपेक्षा शोधित किये जा रहे सोमरस के गुणों का वर्णन करो
- **Translation**: 

---

### Verse 19 (Sama Ved 0.1979)
- **Original**: इ्ति पञ्चम: खण्ड:
- **Translation**: 

---

### Verse 20 (Sama Ved 0.1980)
- **Original**: षष्ठ: खण्ड:
- **Translation**: 

---

