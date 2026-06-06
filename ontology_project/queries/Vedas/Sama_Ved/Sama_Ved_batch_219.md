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

### Verse 1 (Sama Ved 0.4361)
- **Original**: इति अष्टादशोउ ध्याय:
- **Translation**: 

---

### Verse 2 (Sama Ved 0.4362)
- **Original**: जा उन -क्फेन 10न+ -+
- **Translation**: 

---

### Verse 3 (Sama Ved 0.4363)
- **Original**: अथ एकोनविंशो5 ध्याय:
- **Translation**: 

---

### Verse 4 (Sama Ved 0.4364)
- **Original**: प्रथम: खण्ड:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.4365)
- **Original**: 17191. अग्नि: प्रलेन जन्मना शुम्भानस्तन्वां3 स्वाम्‌ । कविर्विष्रेण बाबृधे
- **Translation**: 

---

### Verse 6 (Sama Ved 0.4366)
- **Original**: अपने तेजस्वी रूप में सुशोभित होने वाले मेधावी अग्निदेव को पुरातन स्तोत्रों से ऋत्विजों द्वारा प्रज्वलित किया जाता है
- **Translation**: 

---

### Verse 7 (Sama Ved 0.4367)
- **Original**: 1712. ऊर्जो नपातमा हुवे5ग्नि पावकशोचिषम _। अस्समिन्यज्ञे स्वघ्वरे
- **Translation**: 

---

### Verse 8 (Sama Ved 0.4368)
- **Original**: ऊर्जा को नीचे न गिरने देने वाले, पवित्र बनाने वाले दीप्तिमान्‌ अग्निदेव का इस उत्तम यज्ञ में हम आवाहन करते हैं
- **Translation**: 

---

### Verse 9 (Sama Ved 0.4369)
- **Original**: 1713. स नो मित्रमहस्त्वमग्ने शुक्रेण शोचिषा । देवैरा सत्सि बर्हिषि
- **Translation**: 

---

### Verse 10 (Sama Ved 0.4370)
- **Original**: हे पूज्य मित्र तुल्य अग्निदेव ! आप शुप्र ज्वालाओं और तेज से पूर्ण होकर (प्रज्वलितरूप में) देवों के साथ इस यज्ञ में प्रतिष्ठत हों
- **Translation**: 

---

### Verse 11 (Sama Ved 0.4371)
- **Original**: 1714. उत्ते शुष्मासो अस्थू रक्षो भिन्दन्तो अद्विवः । नुदस्व या : परिस्पृथ:
- **Translation**: 

---

### Verse 12 (Sama Ved 0.4372)
- **Original**: हे पाषाणों से कूटे शुद्ध सोम ! आपकी उठती बल तरंगों से राक्षसों का विनाश होता है । आप हमसे संघर्ष करे वाले शत्रुओं को दूर करें
- **Translation**: 

---

### Verse 13 (Sama Ved 0.4373)
- **Original**: 1715. अया निजध्निरोजसा रथसजड़े घने हिते । स्तवा अबिभ्युषा हृदा
- **Translation**: 

---

### Verse 14 (Sama Ved 0.4374)
- **Original**: है सोमदेब ! आप अपनी सामर्थ्य से शत्रु के विध्वंसक हैं । रथों के युद्ध में शत्रुओं का ध्वंस होने पर, हम निर्भय अन्तःकरण से धन प्राप्ति के लिए आपकी स्तुति करते हैं
- **Translation**: 

---

### Verse 15 (Sama Ved 0.4375)
- **Original**: 1716. अस्य ब्रतानि नाधूषे पवमानस्य दूद्या । रुज यस्त्वा पृतन्यति
- **Translation**: 

---

### Verse 16 (Sama Ved 0.4376)
- **Original**: इस संस्कारित सोम के कर्मों से दुष्ट राक्षसों की प्रगति नहीं हो सकती ।हे सोमदेव ! आपके विरुद्ध युद्धाकांक्षी शत्रुओं का आप विनाश करें
- **Translation**: 

---

### Verse 17 (Sama Ved 0.4377)
- **Original**: 1717. त॑ हिन्वन्ति मदच्युतं हरिं नदीषु वाजिनम्‌। इन्दु मिन्द्राय मत्सरम्‌
- **Translation**: 

---

### Verse 18 (Sama Ved 0.4378)
- **Original**: आनन्द रस बहाने वाले, बल और उत्साहवर्द्धक इस हरिताभ सोम को, नदियों (जल) के माध्यम से इन्द्रदेव के लिए प्रेरित करते हैं
- **Translation**: 

---

### Verse 19 (Sama Ved 0.4379)
- **Original**: 9798, आ मन्द्रैरित्न हरिभि्याहि मयूररोमभि: । मा त्वा के चिन्नि येमुरिन्‍्न पाशिनो5ति धन्वेव ताँ इहि
- **Translation**: 

---

### Verse 20 (Sama Ved 0.4380)
- **Original**: हे इन्द्रदेव ! आनन्ददायक, मोर पंखों के समान बालों वाले घोड़ों (किरणों) सहित आप यज्ञ में पधारें । शिकारी की तरह मार्ग में जाल फैलाने वाले आपको रोक न पाएँ, उन्हें रेगिस्तान (मृग- मरोंबिका) की तरह छोड़कर आएँ
- **Translation**: 

---

